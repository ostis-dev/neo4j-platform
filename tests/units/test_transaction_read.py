from sc.transaction.read import AssignParameter, FixedParameter
from unittest import result
import sc
from tests.memory_case import MemoryTestCase

class TestFindTemplate(MemoryTestCase):

  def test_find_triple(self):
    tr = self.memory.create_write_transaction()
    src = tr.create_node("src")
    trg = tr.create_node("trg")
    edge = tr.create_edge(src, trg, "sc_edge", "edge")
    result = tr.run()

    self.assertEqual(len(result), 3)
    src = result[src]
    trg = result[trg]
    edge = result[edge]

    tr = self.memory.create_read_transaction()
    _src, _edge, _trg = tr.triple_faa(FixedParameter(src, "src"), AssignParameter("sc_edge", "edge"), AssignParameter(None, "trg"))
    result = tr.run()

    self.assertEqual(len(result), 1)
    items = result[0]

    self.assertEqual(items[_src], src)
    self.assertEqual(items[_trg], trg)
    self.assertEqual(items[_edge], edge)

  def test_find_constr_5(self):
    tr = self.memory.create_write_transaction()
    src = tr.create_node("src")
    trg = tr.create_node("trg")
    attr = tr.create_node("attr")

    edge = tr.create_edge(src, trg, "sc_edge", "edge")
    attr_edge = tr.create_edge(attr, edge, "sc_edge", "attr_edge")

    result = tr.run()
    self.assertEqual(len(result), 5)
    src = result[src]
    trg = result[trg]
    attr = result[attr]
    edge = result[edge]
    attr_edge = result[attr_edge]

    tr = self.memory.create_read_transaction()
    _src, _edge, _trg = tr.triple_faf(FixedParameter(src, "src"), AssignParameter("sc_edge", "edge"), FixedParameter(trg, "trg"))
    _attr, _attr_edge, _ = tr.triple_faf(FixedParameter(attr, "attr"), AssignParameter("sc_edge", "attr_edge"), _edge)

    result = tr.run()
    
    self.assertEqual(len(result), 1)

    items = result[0]
    self.assertEqual(items[_src], src)
    self.assertEqual(items[_trg], trg)
    self.assertEqual(items[_edge], edge)
    self.assertEqual(items[_attr], attr)
    self.assertEqual(items[_attr_edge], attr_edge)

  def test_find_constr_5_edge_first(self):
    tr = self.memory.create_write_transaction()
    src = tr.create_node("src")
    trg = tr.create_node("trg")
    attr = tr.create_node("attr")

    edge = tr.create_edge(src, trg, "sc_edge", "edge")
    attr_edge = tr.create_edge(attr, edge, "sc_edge", "attr_edge")

    result = tr.run()
    self.assertEqual(len(result), 5)
    src = result[src]
    trg = result[trg]
    attr = result[attr]
    edge = result[edge]
    attr_edge = result[attr_edge]

    tr = self.memory.create_read_transaction()
    _src, _edge, _trg = tr.triple_afa(AssignParameter(None, "src"), FixedParameter(edge, "edge"), AssignParameter(None, "trg"))
    _attr, _attr_edge, _ = tr.triple_faf(FixedParameter(attr, "attr"), AssignParameter("sc_edge", "attr_edge"), _edge)

    result = tr.run()

    self.assertEqual(len(result), 1)

    items = result[0]
    self.assertEqual(items[_src], src)
    self.assertEqual(items[_trg], trg)
    self.assertEqual(items[_edge], edge)
    self.assertEqual(items[_attr], attr)
    self.assertEqual(items[_attr_edge], attr_edge)
    