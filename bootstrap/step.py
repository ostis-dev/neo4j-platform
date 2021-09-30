import jinja2
import neo4j

from sc.labels import Labels
from sc.keynodes import Keynodes
from sc.config import Config

from typing import Union

class Step:

  def __init__(self, driver: neo4j.Driver, templ: jinja2.Template, config: Config) -> None:
    self._driver = driver
    self._config = config
    self._error = None
    self._query = self._load_query(templ)
  
  @property
  def error(self) -> str:
    return self._error

  def _load_query(self, templ: jinja2.Template) -> str:
    return templ.render(Keynodes=Keynodes, Labels=Labels)

  def run(self) -> neo4j.ResultSummary:

    # print (self._query)
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