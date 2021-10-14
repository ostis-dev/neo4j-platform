from sc.core.types import ElementID
from sc.core.keynodes import Keynodes
from sc.core.keywords import Labels, TypeAttrs

import neo4j


def _const_attr() -> str:
    return f"{TypeAttrs.CONST}: 'CONST'"


def _arc_member_const_pos_perm_attrs() -> str:
    return f"{TypeAttrs.CONST}: 'CONST', {TypeAttrs.ARC_PERM}: 'PERM', {TypeAttrs.ARC_POS}: 'POS'"


class TransactionNamesWriteResult:

    def __init__(self, result_summary: neo4j.ResultSummary):
        self.run_time = result_summary.result_available_after
        self.consume_time = result_summary.result_consumed_after

    def __repr__(self) -> str:
        return "run_time: {} ms, consume_time: {} ms".format(
            self.run_time,
            self.consume_time
        )


class TransactionNamesWrite:

    def __init__(self,
                 driver: neo4j.Driver,
                 nrel_sys_idtf: str = Keynodes.NREL_SYS_IDTF) -> None:
        self._driver = driver
        self._sys_idtfs = set()
        self._tasks = []

        self._nrel_sys_idtf = nrel_sys_idtf

        assert isinstance(self._nrel_sys_idtf, str)

    def set_system_identifier(self, el: ElementID, sys_idtf: str):
        """
        Adds command to setup system identifier of specified element.
        If element already have system_identifier, then it will be replaces with new one

        :param el: Element id to setup system identifier
        :params sys_idtf: Value of system identifier
        """
        assert sys_idtf not in self._sys_idtfs

        self._sys_idtfs.add(sys_idtf)
        self._tasks.append((el, sys_idtf))

    def _is_empty(self) -> bool:
        return len(self._sys_idtfs) == 0

    def _make_query(self) -> str:
        query = (f"MATCH (l:{Labels.SC_LINK} {{content: '{Keynodes.NREL_SYS_IDTF}', {_const_attr()} }})"
                 f"<-[__idtf_edge:{Labels.SC_ARC} {{ {TypeAttrs.CONST}: 'CONST' }}]"
                 f"-(__sys_idtf:{Labels.SC_NODE}), \n"
                 f"(:{Labels.SC_EDGE_SOCK} {{edge_id: id(__idtf_edge)}})"
                 f"<-[:{Labels.SC_ARC_MEMBER} {{ {_arc_member_const_pos_perm_attrs()} }}]"
                 f"-(__sys_idtf)\n")

        def _subquery_item(task):
            el, idtf = task

            return (f"\n  MATCH (el:{el.label}) WHERE id(el) = {el.id}\n"
                    f"  OPTIONAL MATCH (el)"
                    f"-[edge:{Labels.SC_ARC} {{ {_const_attr()} }}]"
                    f"->(link: {Labels.SC_LINK} {{ {_const_attr()} }}),\n"
                    f"  (edge_sock: {Labels.SC_EDGE_SOCK} {{ edge_id: id(edge)}})"
                    f"<-[edge_rel:{Labels.SC_ARC_MEMBER} {{ {_arc_member_const_pos_perm_attrs()} }}]"
                    f"-(__sys_idtf)\n"
                    f"  RETURN el, edge_sock, edge, '{idtf}' as idtf\n")

        query += (f"CALL {{"
                  f"{'UNION'.join(map(lambda t: _subquery_item(t), self._tasks))}"
                  f"}}\n"
                  f"WITH el, edge_sock, edge, idtf, __sys_idtf\n"
                  f"DETACH DELETE edge_sock\nDELETE edge\n"
                  f"WITH el, idtf, __sys_idtf\n"
                  f"CREATE (el)"
                  f"-[edge:{Labels.SC_ARC} {{ {_const_attr()} }}]"
                  f"->(:{Labels.SC_LINK} {{ content: idtf, type: 'str', is_url: false, {_const_attr()} }})\n"
                  f"WITH __sys_idtf, edge\n"
                  f"CREATE (: {Labels.SC_EDGE_SOCK} {{edge_id: id(edge)}})"
                  f"<-[:{Labels.SC_ARC_MEMBER} {{ {_arc_member_const_pos_perm_attrs()} }}]"
                  f"-(__sys_idtf)\n"
                  f"RETURN edge")

        return query

    def run(self) -> TransactionNamesWriteResult:
        assert not self._is_empty()

        query = self._make_query()
        # print (query)
        with self._driver.session() as session:
            return session.write_transaction(TransactionNamesWrite._run_impl, query)

    @neo4j.unit_of_work(timeout=30)
    def _run_impl(tx: neo4j.Transaction, query):
        try:
            query_res = tx.run(query)
        except neo4j.exceptions.DriverError:
            return None

        info = query_res.consume()
        return TransactionNamesWriteResult(result_summary=info)

# ------------------------------


class TransactionNamesReadResult:

    def __init__(self, values: dict, result_summary: neo4j.ResultSummary):
        self.values = values
        self.run_time = result_summary.result_available_after
        self.consume_time = result_summary.result_consumed_after

    def __getitem__(self, idtf):
        return self.values[idtf]

    def __len__(self):
        return len(self.values)

    def __repr__(self) -> str:
        return "values_num: {}, run_time: {} ms, consume_time: {} ms".format(
            len(self.values.keys()),
            self.run_time,
            self.consume_time
        )


class TransactionNamesRead:

    def __init__(self,
                 driver: neo4j.Driver,
                 nrel_sys_idtf: str = Keynodes.NREL_SYS_IDTF) -> None:
        self._driver = driver
        self._sys_idtfs = set()

        self._nrel_sys_idtf = nrel_sys_idtf

        assert isinstance(self._nrel_sys_idtf, str)

    def resolve_by_system_identifier(self, sys_idtf: str) -> str:
        """
        Adds command to resolve element by system identifier

        :params sys_idtf: Value of system identifier
        :returns Returns alias of result value. IT shoudl be used to get ElementID from result
        """
        assert sys_idtf not in self._sys_idtfs

        self._sys_idtfs.add(sys_idtf)
        return sys_idtf

    def _is_empty(self) -> bool:
        return len(self._sys_idtfs) == 0

    def _make_query(self) -> str:

        query = (f"MATCH (l:{Labels.SC_LINK} {{ content: '{Keynodes.NREL_SYS_IDTF}', {_const_attr()} }})"
                 f"<-[edge:{Labels.SC_ARC} {{ {_const_attr()} }}]"
                 f"-(__sys_idtf:{Labels.SC_NODE}), \n"
                 f"(edge_sock:{Labels.SC_EDGE_SOCK} {{edge_id: id(edge)}})"
                 f"<-[:{Labels.SC_ARC_MEMBER} {{ {_arc_member_const_pos_perm_attrs()} }}]"
                 f"-(__sys_idtf)\n"
                 f"WITH __sys_idtf\n")

        with_values = ["__sys_idtf"]
        for idtf in self._sys_idtfs:
            if len(with_values) > 1:
                query += "UNION\n"

            with_values.append(idtf)
            query += (f"MATCH (link:{Labels.SC_LINK} {{ content: '{idtf}', {_const_attr()} }}),"
                      f" ({idtf})-[edge:{Labels.SC_ARC} {{ {_const_attr()} }}] -> (link), \n"
                      f"(__sys_idtf)-[:{Labels.SC_ARC_MEMBER} {{ {_arc_member_const_pos_perm_attrs()} }}]->(:{Labels.SC_EDGE_SOCK} {{edge_id: id(edge)}})\n"
                      f"RETURN '{idtf}' as idtf, {idtf} as el\n")

        return query

    def run(self) -> TransactionNamesReadResult:
        assert not self._is_empty()

        query = self._make_query()
        # print (query)
        with self._driver.session() as session:
            return session.write_transaction(TransactionNamesRead._run_impl, query)

    @neo4j.unit_of_work(timeout=10)
    def _run_impl(tx: neo4j.Transaction, query):
        try:
            query_res = tx.run(query)
        except neo4j.exceptions.DriverError:
            return None

        values = {}
        for _, record in enumerate(query_res):
            key = record["idtf"]
            value = record["el"]

            if isinstance(value, neo4j.graph.Relationship):
                values[key] = ElementID(value.type, value.id)
            elif isinstance(value, neo4j.graph.Node):
                label, = value.labels
                values[key] = ElementID(label, value.id)

        info = query_res.consume()

        return TransactionNamesReadResult(values, result_summary=info)
