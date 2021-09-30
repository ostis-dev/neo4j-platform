from sc.types import ElementID
from sc.keynodes import Keynodes

import neo4j

class TransactionNamesWrite:

  class Result:
    def __init__(self, elements: dict) -> None:
      self._elements = elements
    
    def __getitem__(self, name) -> ElementID:
      return self._elements[name]

    def __len__(self):
      return len(self._elements)

    def __repr__(self) -> str:
      return f'TransactionNamesWrite({self._elements})'
    
  def __init__(self,
               driver: neo4j.Driver, 
               nrel_sys_idtf: str = Keynodes.NREL_SYS_IDTF) -> None:
    self._driver = driver
    self._sys_idtf = set()

    self._nrel_sys_idtf = nrel_sys_idtf

    assert isinstance(self._nrel_sys_idtf, str)

  def resolve_by_sys_idtf(self, sys_idtf: str):
    self._sys_idtf.add(sys_idtf)

  def _is_empty(self) -> bool:
    return len(self._sys_idtf) == 0

  def _make_query(self) -> str:
    pass

  def run(self):
    assert  not self._is_empty()

    query = self._make_query()
    # print (query)
    with self.driver.session() as session:
      return session.write_transaction(TransactionNamesWrite._run_impl, query)

  @neo4j.unit_of_work(timeout=30)
  def _run_impl(tx: neo4j.Transaction, query):
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