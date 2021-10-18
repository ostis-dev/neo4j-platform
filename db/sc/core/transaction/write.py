import sc.core.types as types

from sc.core.element import Edge, ElementID, Element
from sc.core.types import NodeType, EdgeType, ArcType, LinkType, TypeArcPerm
from sc.core.keywords import Labels
from sc.core.transaction.utils import _parse_output_element

from typing import Union

import neo4j


class TransactionWriteResult:

    def __init__(self, values: dict, result_summary: neo4j.ResultSummary):
        self.values = values
        self.run_time = result_summary.result_available_after
        self.consume_time = result_summary.result_consumed_after

    def __getitem__(self, alias) -> Element:
        return self.values[alias]

    def __len__(self):
        return len(self.values)

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"values_num: {len(self.values.keys())}, "
                f"run_time: {self.run_time} ms, "
                f"consume_time: {self.consume_time} ms, "
                f"items: {self.values})")


class TransactionWrite:

    def __init__(self, driver: neo4j.Driver):
        self.driver = driver

        self._id_counter = 0
        self._id_to_alias = {}
        self._nodes_to_create = []
        self._edges_to_create = []
        self._links_to_create = []
        self._edge_aliases = set()
        self._results = {}

    def _next_id(self):
        self._id_counter += 1
        return self._id_counter

    def _process_alias(self, alias: str, label: str, prefix="el"):
        if alias is None:
            alias = f"{prefix}_{self._next_id()}"
            self._results[alias] = label
            return alias

        if alias in self._results:
            raise KeyError(f"Alias {alias} already exist")

        self._results[alias] = label
        return alias

    def create_node(self, type: NodeType, alias=None) -> str:
        assert isinstance(type, NodeType)
        alias = self._process_alias(alias, Labels.SC_NODE, prefix="node")
        self._nodes_to_create.append((alias, Labels.SC_NODE, type._to_attrs()))
        return alias

    def create_link_with_content(self,
                                 type: LinkType,
                                 alias: str = None,
                                 content: Union[str, int, float] = None,
                                 is_url: bool = False):

        assert isinstance(type, LinkType)
        alias = self._process_alias(alias, Labels.SC_LINK, prefix="link")
        self._links_to_create.append(
            (alias, Labels.SC_LINK, is_url, content, type._to_attrs()))
        return alias

    def _resolve_alias_by_element_id(self, el_id: ElementID):
        assert isinstance(el_id, ElementID)
        try:
            return self._id_to_alias[el_id.full_id]
        except KeyError:
            alias = f"el_{self._next_id()}"
            self._id_to_alias[el_id.full_id] = (alias, el_id)
            return alias

    def create_edge(self,
                    src: Union[str, Element],
                    trg: Union[str, Element],
                    type: Union[ArcType, EdgeType],
                    alias: str = None,) -> str:

        label = None
        if isinstance(type, ArcType):
            label = Labels.SC_ARC
        elif isinstance(type, EdgeType):
            label = Labels.SC_EDGE
        else:
            raise TypeError("Unknown edge type: {type}")

        alias = self._process_alias(alias, label, prefix="edge")

        src_alias = src if isinstance(
            src, str) else self._resolve_alias_by_element_id(src.id)
        trg_alias = trg if isinstance(
            trg, str) else self._resolve_alias_by_element_id(trg.id)

        self._edges_to_create.append(
            (alias, src_alias, trg_alias, label, type._to_attrs()))
        self._edge_aliases.add(alias)

        return alias

    def _make_query(self) -> str:
        query = ""

        # resolve nodes
        if len(self._id_to_alias) > 0:
            query += "MATCH "
            query += ", ".join(
                [f"({v[0]}:{v[1].label})" for v in self._id_to_alias.values()])
            query += "\nWHERE "
            query += " AND ".join([f"id({value[0]})={value[1].identity}" for _,
                                  value in self._id_to_alias.items()])

        def _make_attrs(attrs):
            if attrs is not None and len(attrs) > 0:
                return " { " + ', '.join([f"{key}: '{value}'" for key, value in attrs.items()]) + " }"

            return ""

        # create nodes and edges
        create_nodes = ", ".join(
            [f"({alias}:{label}{_make_attrs(attrs)})" for alias, label, attrs in self._nodes_to_create])
        create_sockets = ", ".join(
            [f"({v[0]}_sock:{Labels.SC_EDGE_SOCK})" for v in self._edges_to_create])

        def _process_edge_alias(alias):
            if alias in self._edge_aliases:
                return f'{alias}_sock'
            return alias

        create_edges = ", ".join([
            f"({_process_edge_alias(src_alias)})-[{alias}:{label}{_make_attrs(attrs)}]->({_process_edge_alias(trg_alias)})"
            for alias, src_alias, trg_alias, label, attrs in self._edges_to_create
        ])

        # create links
        def _create_link(link: tuple):
            alias, label, is_url, content, attrs = link
            if is_url:
                assert isinstance(content, str)

            type = "unknown"
            if isinstance(content, str):
                type = "str"
            elif isinstance(content, int):
                type = "int"
            elif isinstance(content, float):
                type = "float"

            is_url = 1 if is_url else 0

            def _make_link_attrs(attrs):
                if attrs is not None and len(attrs) > 0:
                    return ", " + ", ".join([f"{key}: '{value}'" for key, value in attrs.items()])

                return ""

            return f"({alias}:{label} {{ content: '{content}', is_url: '{is_url}', type: '{type}' {_make_link_attrs(attrs)}}})"

        create_links = ", ".join([_create_link(link)
                                  for link in self._links_to_create])

        create_params = ""
        if len(create_nodes) > 0:
            create_params = create_nodes

        if len(create_links) > 0:
            if len(create_params) > 0:
                create_params += ","
            create_params += create_links

        if len(create_edges) > 0:
            if len(create_params) > 0:
                create_params += ", "
            create_params += create_sockets + ", " + create_edges

        if len(create_params) > 0:
            query += "\nCREATE " + create_params

        # create sockets
        if len(create_edges) > 0:
            def _build_edge_aliases(item):
                alias, label = item
                if label == Labels.SC_ARC or label == Labels.SC_EDGE:
                    return f"{alias}_sock, {alias}"

                return alias

            # build with command
            with_values = "\nWITH " + \
                ", ".join(
                    map(lambda r: f"{_build_edge_aliases(r)}", self._results.items()))
            query += with_values
            query += "\nSET " + \
                ", ".join(map(
                    lambda edge: f"{edge[0]}_sock.edge_id = id({edge[0]})", self._edges_to_create))

        if len(self._results) > 0:
            query += "\nRETURN " + \
                ", ".join(map(lambda r: f"{r}", self._results.keys()))
        else:
            query += "\nRETURN null"

        return query

    def _is_empty(self) -> bool:
        return (
            len(self._nodes_to_create) == 0 and
            len(self._edges_to_create) == 0 and
            len(self._links_to_create) == 0
        )

    def run(self) -> TransactionWriteResult:
        if self._is_empty():
            return None

        query = self._make_query()
        with self.driver.session() as session:
            return session.write_transaction(TransactionWrite._run_impl, query, self._results)

    @ neo4j.unit_of_work(timeout=30)
    def _run_impl(tx: neo4j.Transaction, query, results):
        try:
            query_res = tx.run(query)
        except neo4j.exceptions.DriverError:
            return None

        values = {}
        for ix, record in enumerate(query_res):
            assert ix == 0
            for key, item in record.items():
                if key == "null":
                    continue

                values[key] = _parse_output_element(item=item)

        info = query_res.consume()
        result = TransactionWriteResult(values=values, result_summary=info)

        return result
