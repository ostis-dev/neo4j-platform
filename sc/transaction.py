from typing import Union

import neo4j
from neo4j.exceptions import TransactionError

from sc.commands import CreateNodeCommand

class TransactionResult:
  def __init__(self, values: dict, result_summary: neo4j.ResultSummary):
    self.values = values
    self.run_time = result_summary.result_available_after
    self.consume_time = result_summary.result_consumed_after

  def __getitem__(self, alias):
    return self.values[alias]
  

class TransactionWrite:

  def __init__(self, driver: neo4j.Driver):
    self.commands = []
    self.results = []
    self.driver = driver

  def generate_tmp_alias(self, prefix = "el"):
    return "{}_{}".format(prefix, len(self.commands))

  def create_node(self, alias = None) -> str:
    name = alias
    if alias is None:
      name = self.generate_tmp_alias("node")
    else:
      self.results.append(alias)

    self.commands.append(CreateNodeCommand(name=name))

  def _make_query(self) -> str:
    query = ""
    for cmd in self.commands:
      query += cmd.generate() + "\n"

    query += "RETURN " + ",".join(map(lambda r: "id({}) as {}".format(r, r), self.results))

    return query

  def run(self) -> TransactionResult:
    query = self._make_query()

    with self.driver.session() as session:
      return session.write_transaction(TransactionWrite._run_impl, query)

  @neo4j.unit_of_work(timeout=5)
  def _run_impl(tx: neo4j.Transaction, query):
    try:
      query_res = tx.run(query)
    except TransactionError:
      return None

    values = {}
    for ix, record in enumerate(query_res):
      assert ix == 0
      for key, value in record.items():
        values[key] = value

    info = query_res.consume()
    result = TransactionResult(values=values, result_summary=info)

    return result