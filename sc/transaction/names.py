from sc import labels
from sc.types import ElementID
from sc.keynodes import Keynodes
from sc.labels import Labels

import neo4j

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
    query = (f"MATCH (l:{Labels.SC_LINK} {{content: '{Keynodes.NREL_SYS_IDTF}'}})<-[edge:{Labels.SC_EDGE}]-(__sys_idtf:{Labels.SC_NODE}), \n"
             f"(edge_sock:{Labels.SC_EDGE_SOCK} {{edge_id: id(edge)}})<-[:{Labels.SC_EDGE}]-(__sys_idtf)\n")
    query += "WITH __sys_idtf\n"

    for el, idtf in self._tasks:
      query += (f"MATCH (el:{el.label}) WHERE id(el) = {el.id}\n"
                f"WITH el, __sys_idtf\n"
                f"OPTIONAL MATCH (el)-[edge:{Labels.SC_EDGE}]->(link: {Labels.SC_LINK}),\n"
                f"(__sys_idtf)-[edge_rel:{Labels.SC_EDGE}]->(edge_sock: {Labels.SC_EDGE_SOCK} {{ edge_id: id(edge)}})\n"
                f"WITH el, edge_sock, edge, __sys_idtf\n"
                f"DETACH DELETE edge_sock\nDELETE edge\n"
                f"WITH __sys_idtf, el\n"
                f"CREATE (el)-[edge:{Labels.SC_EDGE}]->(link:{Labels.SC_LINK} {{content: '{idtf}', type: 'str', is_url: false}})\n"
                f"WITH __sys_idtf, edge\n"
                f"CREATE (edge_sock: {Labels.SC_EDGE_SOCK} {{edge_id: id(edge)}}), (__sys_idtf)-[:{Labels.SC_EDGE}]->(edge_sock)\n"
                f"WITH __sys_idtf\n")
      
    query += "RETURN null"

    return query

  def run(self) -> TransactionNamesWriteResult:
    assert  not self._is_empty()

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

    query = (f"MATCH (l:{Labels.SC_LINK} {{content: '{Keynodes.NREL_SYS_IDTF}'}})<-[edge:{Labels.SC_EDGE}]-(__sys_idtf:{Labels.SC_NODE}), \n"
             f"(edge_sock:{Labels.SC_EDGE_SOCK} {{edge_id: id(edge)}})<-[:{Labels.SC_EDGE}]-(__sys_idtf)\n"
             f"WITH __sys_idtf\n")

    with_values = ["__sys_idtf"]
    for idtf in self._sys_idtfs:
      with_values.append(idtf)
      query += (f"OPTIONAL MATCH ({idtf}_link:{Labels.SC_LINK} {{content: '{idtf}'}})<-[{idtf}_edge:{Labels.SC_EDGE}]-({idtf}),\n"
                f"(:{Labels.SC_EDGE_SOCK} {{edge_id: id({idtf}_edge)}})<-[:{Labels.SC_EDGE}]-(__sys_idtf)\n"
                f"WITH {', '.join(with_values)}\n")

    query += "RETURN " + ", ".join(map(lambda r: f"{r}", self._sys_idtfs))

    return query

  def run(self) -> TransactionNamesReadResult:
    assert  not self._is_empty()

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
    for ix, record in enumerate(query_res):
      assert ix == 0
      for key, value in record.items():
        if key == "null":
          continue
      
        if isinstance(value, neo4j.graph.Relationship):
          values[key] = ElementID(value.type, value.id)  
        elif isinstance(value, neo4j.graph.Node):
          label, = value.labels
          values[key] = ElementID(label, value.id)

    info = query_res.consume()

    return TransactionNamesReadResult(values, result_summary=info)
