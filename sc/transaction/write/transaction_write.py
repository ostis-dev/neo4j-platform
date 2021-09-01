from logging import NullHandler
from typing import Union

import neo4j
from neo4j.exceptions import TransactionError

class TransactionResult:
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
    self._results = []

  def _next_id(self):
    self._id_counter += 1
    return self._id_counter

  def _process_alias(self, alias, prefix = "el"):
    if alias is None:
      return f"{prefix}_{self._next_id()}"
    
    if alias in self._results:
      raise KeyError(f"Alias {alias} already exist")

    self._results.append(alias)
    return alias

  def create_node(self, alias = None) -> str:
    alias = self._process_alias(alias, prefix="node")
    self._nodes_to_create.append((alias, "sc_node"))
    return alias

  def _resolve_alias_by_id(self, id):
    assert isinstance(id, int)
    try:
      return self._id_to_alias[id]
    except KeyError:
      alias = f"el_{self._next_id()}"
      self._id_to_alias[id] = alias
      return alias

  def create_edge(self, src: Union[str, int], trg: Union[str, int], alias = None) -> str:
    alias = self._process_alias(alias, prefix="edge")
    self._nodes_to_create.append((alias, "sc_edge"))

    src_alias = src if isinstance(src, str) else self._resolve_alias_by_id(src)
    trg_alias = trg if isinstance(trg, str) else self._resolve_alias_by_id(trg)

    self._edges_to_create.append((alias, src_alias, "sc_connect_src"))
    self._edges_to_create.append((alias, trg_alias, "sc_connect_trg"))

    return alias

  def _make_query(self) -> str:
    query = ""

    # resolve nodes
    if len(self._id_to_alias) > 0:
      query += "MATCH "
      query += ", ".join([f"({alias})" for alias in self._id_to_alias.values()])
      query += "\nWHERE "
      query += " AND ".join([f"id({alias})={id}" for id, alias in self._id_to_alias.items()])

    # create nodes and edges
    query += "\nCREATE "
    query += ", ".join([f"({alias}:{label})" for alias, label in self._nodes_to_create])

    if len(self._nodes_to_create) > 0 and len(self._edges_to_create) > 0:
      query += ", "
      query += ", ".join([
        f"({src_alias})-[:{label}]->({trg_alias})" for src_alias, trg_alias, label in self._edges_to_create
        ])

    if len(self._results) > 0:
      query += "\nRETURN " + ",".join(map(lambda r: "id({}) as {}".format(r, r), self._results))
    else:
      query += "\nRETURN null"

    return query

  def run(self) -> TransactionResult:

    if len(self._nodes_to_create) == 0 and len(self._edges_to_create) == 0:
      return None

    query = self._make_query()

    print ("-" * 20)
    print (query)
    with self.driver.session() as session:
      return session.write_transaction(TransactionWrite._run_impl, query)

  @neo4j.unit_of_work(timeout=30)
  def _run_impl(tx: neo4j.Transaction, query):
    try:
      query_res = tx.run(query)
    except TransactionError:
      return None

    values = {}
    for ix, record in enumerate(query_res):
      assert ix == 0
      for key, value in record.items():
        if key == "null":
          continue
        values[key] = int(value)

    info = query_res.consume()
    result = TransactionResult(values=values, result_summary=info)

    return result