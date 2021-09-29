import neo4j

from sc.labels import Labels
from sc.keynodes import Keynodes

from string import Template
from sc.config import Config
from typing import Union

class Step:

  def __init__(self, driver: neo4j.Driver, file_name: str, config: Config) -> None:
    self._driver = driver
    self._config = config
    self._error = None
    self._query = self._load_query(file_name)  
  
  @property
  def error(self) -> str:
    return self._error

  def _load_query(self, file_name: str) -> str:
    params = {
      "database_name": self._config.db_name(),

      "sc_edge": Labels.SC_EDGE,
      "sc_edge_sock": Labels.SC_EDGE_SOCK,
      "sc_link": Labels.SC_LINK,
      "sc_node": Labels.SC_NODE,

      "nrel_sys_idtf": Keynodes.NREL_SYS_IDTF,
    }

    query = open(file_name).read()
    return Template(query).substitute(params)

  def run(self) -> neo4j.ResultSummary:
    with self._driver.session() as session:
      result = session.write_transaction(Step._run_impl, self._query)

      if isinstance(result, neo4j.ResultSummary):
        return result
      else:
        return None

  @neo4j.unit_of_work(timeout=30)
  def _run_impl(tx: neo4j.Transaction, query) -> Union[neo4j.ResultSummary, str]:
    try:
      query_res = tx.run(query)
    except neo4j.exceptions.DriverError as err:
      return err.message

    return query_res.consume()
  
  def error(self, desciption: str):
    self._error = desciption