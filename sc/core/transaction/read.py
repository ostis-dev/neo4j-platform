import neo4j

from sc.core.types import ElementID
from sc.core.labels import Labels

from enum import Enum
from typing import Union, Tuple

class FixedParameter:

  def __init__(self, el_id: ElementID, alias: str = None):
    self._el_id = el_id
    self._alias = alias

  @property
  def id(self):
    return self._el_id

  @property
  def alias(self):
    return self._alias

  def __repr__(self) -> str:
    return f'FixedParameter(id: {self.id}, alias: {self.alias})'

class AssignParameter:

  def __init__(self, label: str, alias: str = None):
    self._label = label
    self._alias = alias
  
  @property
  def label(self):
    return self._label

  @property
  def alias(self):
    return self._alias

  def __repr__(self) -> str:
    return f'FixedParameter(label: {self.label}, alias: {self.alias})'

class TransactionReadResult:

  class Item:
    def __init__(self, values: dict):
      self._values = values

    def __getitem__(self, alias):
      return self._values[alias]

    def __len__(self):
      return len(self._values)

    def __repr__(self) -> str:
      return f'Item({self._values})'

  def __init__(self, result_summary: neo4j.ResultSummary):
    self.items = []
    self.run_time = result_summary.result_available_after
    self.consume_time = result_summary.result_consumed_after

  def _add_item(self, item):
    assert isinstance(item, TransactionReadResult.Item)
    self.items.append(item)

  def __getitem__(self, idx: int):
    assert idx < len(self.items)
    return self.items[idx]

  def __len__(self):
    return len(self.items)

  def __iter__(self):
    return iter(self.items)

  def __repr__(self) -> str:
    return "items_num: {}, run_time: {} ms, consume_time: {} ms".format(
      len(self.items),
      self.run_time,
      self.consume_time
    )

class TransactionRead:

  class TripleType(Enum):
    FAA = 0
    AFA = 1
    AAF = 2
    FAF = 3

  def __init__(self, driver: neo4j.Driver):
    self._driver = driver
    self._triples = []

    self._id_to_alias = {}
    self._aliases = set()
    self._result = set() # set of aliases that should be in result
    self._edges = set() # set of edge aliases
    self._edge_require_sock = set() # set of edges that require socket

  def _process_alias(self, element: Union[FixedParameter, AssignParameter]) -> str:
    result_alias = None
    if isinstance(element, FixedParameter):
      alias = element.alias
      try:
        alias = self._id_to_alias[element.id.full_id][0]
        if alias != element.alias:
          raise f"Element `{element.id.full_id}` already exist with alias `{alias}`"
      except KeyError:
        if alias is None:
          alias = f'f_{len(self._id_to_alias)}'
        else:
          self._result.add(alias)
        
        self._id_to_alias[element.id.full_id] = (alias, element.id)

      result_alias = alias
    elif isinstance(element, AssignParameter):
      if element.alias is not None:
        self._result.add(element.alias)
        result_alias = element.alias
      else:
        result_alias = f'a_{len(self._aliases)}'
    else:
      raise "Unsupported element type"

    assert result_alias is not None
    self._aliases.add(result_alias)
    return result_alias

  def _check_alias_exists(self, alias):
    if len(alias) == 0:
      raise "Alias coldn't be empty"

    if not alias in self._aliases:
      raise "There are no element with alias {alias}"

  def triple_faa(self, source: Union[str, FixedParameter], edge: AssignParameter, target: AssignParameter) -> Tuple:
    source_alias = None
    if isinstance(source, str):
      source_alias = source
      self._check_alias_exists(source)
    elif isinstance(source, FixedParameter):
      source_alias = self._process_alias(source)
    else:
      raise f"Unsupported type of `source` parameter - {type(source)}"

    edge_alias = self._process_alias(edge)
    target_alias = self._process_alias(target)

    self._edges.add(edge_alias)

    assert source_alias is not None
    assert target_alias is not None

    self._triples.append((TransactionRead.TripleType.FAA, source_alias, (edge_alias, edge.label), (target_alias, target.label)))
    return (source_alias, edge_alias, target_alias)

  def triple_aaf(self, source: AssignParameter, edge: AssignParameter, target: Union[str, FixedParameter]) -> Tuple:
    target_alias = None
    if isinstance(target, str):
      target_alias = target
      self._check_alias_exists(target)
    elif isinstance(target, FixedParameter):
      target_alias = self._process_alias(target)
    else:
      raise f"Unsupported type of `target` parameter - {type(target)}"

    edge_alias = self._process_alias(edge)
    source_alias = self._process_alias(source)

    self._edges.add(edge_alias)

    self._triples.append((TransactionRead.TripleType.AAF, (source_alias, source.label), (edge_alias, edge.label), target))
    return (source_alias, edge_alias, target_alias)

  def triple_afa(self, source: AssignParameter, edge: Union[str, FixedParameter], target: AssignParameter) -> Tuple:
    edge_alias = None
    if isinstance(edge, str):
      edge_alias = edge
      self._check_alias_exists(edge)
    elif isinstance(edge, FixedParameter):
      edge_alias = self._process_alias(edge)
    else:
      raise f"Unsupported type of `edge` parameter - {type(edge)}"

    source_alias = self._process_alias(source)
    target_alias = self._process_alias(target)

    self._edges.add(edge_alias)
    
    self._triples.append((TransactionRead.TripleType.AFA, (source_alias, source.label), edge_alias, (target_alias, target.label)))
    return (source_alias, edge_alias, target_alias)

  def triple_faf(self, source: Union[str, FixedParameter], edge: AssignParameter, target: Union[str, FixedParameter]) -> Tuple:
    source_alias = None
    if isinstance(source, str):
      source_alias = source
      self._check_alias_exists(source)  
    elif isinstance(source, FixedParameter):
      source_alias = self._process_alias(source)
    else:
      raise f"Unsupported type of `source` parameter - {type(source)}"

    target_alias = None
    if isinstance(target, str):
      target_alias = target
      self._check_alias_exists(target)
    elif isinstance(target, FixedParameter):
      target_alias = self._process_alias(target)
    else:
      raise f"Unsupported type of `target` parameter - {type(target)}"

    edge_alias = self._process_alias(edge)

    self._edges.add(edge_alias)

    self._triples.append((TransactionRead.TripleType.FAF, source_alias, (edge_alias, edge.label), target_alias))
    return (source_alias, edge_alias, target_alias)

  def _make_query(self) -> str:
    required_sockets = set()
    def _param_to_match(p):
      if isinstance(p, tuple):
        return f'{p[0]}:{p[1]}' if p[1] is not None else p[0]
      return p

    def _process_edge(p):
      if isinstance(p, tuple):
        if p[0] in self._edges:
          required_sockets.add(p[0])
          return (f'{p[0]}_sock:{Labels.SC_EDGE_SOCK}', p[1])
        return p
      
      if p in self._edges:
        required_sockets.add(p)
        return f'{p}_sock:{Labels.SC_EDGE_SOCK}'

      return p

    match_section = "\nMATCH "
    is_first = True
    for t in self._triples:
      _, src, edge, trg = t
      if not is_first:
        match_section += ', '

      src = _process_edge(src)
      trg = _process_edge(trg)
      
      match_section += f'({_param_to_match(src)})-[{_param_to_match(edge)}]->({_param_to_match(trg)})'
      is_first = False

    where_section = "\nWHERE "
    fixed_elements = " AND ".join(map(lambda r: f'id({r[0]}) = {r[1].id}', self._id_to_alias.values()))
    if len(fixed_elements) > 0:
      where_section += fixed_elements
    socket_edges = " AND ".join(map(lambda e: f'{e}_sock.edge_id = id({e})', required_sockets))
    if len(socket_edges) > 0:
      if len(where_section) > 0:
        where_section += " AND "
      where_section += socket_edges

    return_section = "\nRETURN "
    if len(self._result) > 0:
      return_section += ", ".join(map(lambda r: f'{r}', self._result))
    else:
      return_section += " null"

    return match_section + where_section + return_section

  def run(self, limit = 100) -> TransactionReadResult:
    """Run read transaction
    :param limit: Limit number of results. If value is 0 or None, then there are no limit.
    In that case it will be limited by timeout.
    """
    if len(self._triples) == 0:
      return TransactionReadResult()

    query = self._make_query()
    # print (query)
    with self._driver.session() as session:
      return session.write_transaction(TransactionRead._run_impl, query, self._result)

  @neo4j.unit_of_work(timeout=30)
  def _run_impl(tx: neo4j.Transaction, query, result_aliases):
    try:
      query_res = tx.run(query)
    except neo4j.exceptions.DriverError:
      return None

    result_items = []
    for ix, record in enumerate(query_res):
      values = {}

      for key, value in record.items():
        if key == "null":
          continue
        
        if key in result_aliases:
          if isinstance(value, neo4j.graph.Relationship):
            values[key] = ElementID(value.type, value.id)  
          elif isinstance(value, neo4j.graph.Node):
            label, = value.labels
            values[key] = ElementID(label, value.id)

      result_items.append(TransactionReadResult.Item(values))

    info = query_res.consume()
    result = TransactionReadResult(result_summary=info)
    for it in result_items:
      result._add_item(it)

    return result