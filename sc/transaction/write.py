from sc.types import ElementID
from typing import Union

from sc.labels import Labels

import neo4j

class TransactionWriteResult:

  def __init__(self, values: dict, result_summary: neo4j.ResultSummary):
    self.values = values
    self.run_time = result_summary.result_available_after
    self.consume_time = result_summary.result_consumed_after

  def __getitem__(self, alias):
    return self.values[alias]

  def __len__(self):
    return len(self.values)

  def __repr__(self) -> str:
    return "values_num: {}, run_time: {} ms, consume_time: {} ms".format(
      len(self.values.keys()),
      self.run_time,
      self.consume_time
    )

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

  def _process_alias(self, alias: str, label: str, prefix = "el"):
    if alias is None:
      return f"{prefix}_{self._next_id()}"
    
    if alias in self._results:
      raise KeyError(f"Alias {alias} already exist")

    self._results[alias] = label
    return alias

  def create_node(self, alias = None) -> str:
    alias = self._process_alias(alias, Labels.SC_NODE, prefix="node")
    self._nodes_to_create.append((alias, Labels.SC_NODE))
    return alias

  def create_link_with_content(self, alias: str = None, content: Union[str, int, float] = None, is_url: bool = False):
    alias = self._process_alias(alias, Labels.SC_LINK, prefix="link")
    self._links_to_create.append((alias, Labels.SC_LINK, is_url, content))
    return alias

  def _resolve_alias_by_element_id(self, el_id):
    assert isinstance(el_id, ElementID)
    try:
      return self._id_to_alias[el_id.full_id]
    except KeyError:
      alias = f"el_{self._next_id()}"
      self._id_to_alias[el_id.full_id] = (alias, el_id)
      return alias

  def create_edge(self, src: Union[str, ElementID], trg: Union[str, ElementID], edge_label: str, alias: str = None) -> str:
    assert edge_label is not None
    alias = self._process_alias(alias, Labels.SC_EDGE, prefix="edge")

    src_alias = src if isinstance(src, str) else self._resolve_alias_by_element_id(src)
    trg_alias = trg if isinstance(trg, str) else self._resolve_alias_by_element_id(trg)

    self._edges_to_create.append((alias, src_alias, trg_alias, Labels.SC_EDGE))
    self._edge_aliases.add(alias)

    return alias

  def _make_query(self) -> str:
    query = ""

    # resolve nodes
    if len(self._id_to_alias) > 0:
      query += "MATCH "
      query += ", ".join([f"({v[0]}:{v[1].label})" for v in self._id_to_alias.values()])
      query += "\nWHERE "
      query += " AND ".join([f"id({value[0]})={value[1].id}" for id, value in self._id_to_alias.items()])

    # create nodes and edges
    create_nodes = ", ".join([f"({alias}:{label})" for alias, label in self._nodes_to_create])
    create_sockets = ", ".join([f"({v[0]}_sock:{Labels.SC_EDGE_SOCK})" for v in self._edges_to_create])

    def _process_edge_alias(alias):
      if alias in self._edge_aliases:
        return f'{alias}_sock'
      return alias

    create_edges = ", ".join([
      f"({_process_edge_alias(src_alias)})-[{alias}:{label}]->({_process_edge_alias(trg_alias)})" for alias, src_alias, trg_alias, label in self._edges_to_create
      ])

    # create links  
    def _create_link(link: tuple):
      alias, label, is_url, content = link
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

      return f"({alias}:{label} {{ content: '{content}', is_url: '{is_url}', type: '{type}'}})"
    
    create_links = ", ".join([_create_link(link) for link in self._links_to_create])

    create_params = ""    
    if len(create_nodes) > 0:
      create_params = create_nodes
    
    if len(create_edges) > 0:
      if len(create_params) > 0:
        create_params += ", "
      create_params += create_sockets + ", " + create_edges

    if len(create_links) > 0:
      if len(create_params) > 0:
        create_params += ","
      create_params += create_links

    if len(create_params) > 0:
      query += "\nCREATE " + create_params

    # create sockets
    if len(create_edges) > 0:
      def _build_edge_aliases(item):
        alias, label = item
        if label == "sc_edge":
          return f"{alias}_sock, {alias}"
        
        return alias
        
      # build with command
      with_values = "\nWITH " + ", ".join(map(lambda r: f"{_build_edge_aliases(r)}", self._results.items()))
      query += with_values
      query += "\nSET " + ", ".join(map(lambda edge: f"{edge[0]}_sock.edge_id = id({edge[0]})", self._edges_to_create))

    if len(self._results) > 0:
      query += "\nRETURN " + ", ".join(map(lambda r: f"id({r}) as {r}", self._results.keys()))
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
    # print (query)
    with self.driver.session() as session:
      return session.write_transaction(TransactionWrite._run_impl, query, self._results)

  @neo4j.unit_of_work(timeout=30)
  def _run_impl(tx: neo4j.Transaction, query, results):
    try:
      query_res = tx.run(query)
    except neo4j.exceptions.DriverError:
      return None

    values = {}
    for ix, record in enumerate(query_res):
      assert ix == 0
      for key, value in record.items():
        if key == "null":
          continue

        values[key] = ElementID(results[key], value)

    info = query_res.consume()
    result = TransactionWriteResult(values=values, result_summary=info)

    return result