from unittest import result
import sc
from tests.memory_case import MemoryTestCase

class TestConnect(MemoryTestCase):

  def test_duplicate_alias(self):
    tr = self.memory.create_write_transaction()
    tr.create_node("alias")
    self.assertRaises(KeyError, tr.create_node, "alias")

  def test_no_aliases(self):
    tr = self.memory.create_write_transaction()
    tr.create_node()
    tr.create_node()
    result = tr.run()

    self.assertIsNotNone(result)

  def test_create_node_dummy(self):
    tr = self.memory.create_write_transaction()
    name = tr.create_node("alias")
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertEqual(len(result.values), 1)
    self.assertTrue("alias" in result.values)
    self.assertEqual(name, "alias")

  def test_create_nodes(self):
    tr = self.memory.create_write_transaction()
    tr.create_node("alias")
    tr.create_node("alias2")
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertEqual(len(result.values), 2)
    self.assertTrue("alias" in result.values)
    self.assertTrue("alias2" in result.values)

  def test_create_nodes_large(self):
    nodes_num = 100
    tr = self.memory.create_write_transaction()
    for i in range(nodes_num):
      tr.create_node("alias_{}".format(i))
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertEqual(len(result.values), nodes_num)

    for i in range(nodes_num):
      self.assertTrue("alias_{}".format(i) in result.values)

  def test_create_edge_dummy(self):
    tr = self.memory.create_write_transaction()
    src = tr.create_node()
    trg = tr.create_node()
    tr.create_edge(src, trg, "edge")

    result = tr.run()
    self.assertIsNotNone(result)
    self.assertEqual(len(result.values.keys()), 1)
    self.assertTrue("edge" in result.values)

  def test_create_edge_multi_transaction(self):
    tr = self.memory.create_write_transaction()
    src = tr.create_node("src")
    trg = tr.create_node("trg")
    result = tr.run()

    self.assertIsNotNone(result)

    src = result["src"]
    trg = result["trg"]

    self.assertTrue(isinstance(src, int))
    self.assertTrue(isinstance(trg, int))

    tr = self.memory.create_write_transaction()
    tr.create_edge(src, trg, "edge")
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertEqual(len(result), 1)

  def test_create_edge_multi_transaction_src(self):
    tr = self.memory.create_write_transaction()
    src = tr.create_node("src")
    result = tr.run()

    src = result["src"]

    self.assertIsNotNone(result)
    self.assertTrue(isinstance(src, int))

    tr = self.memory.create_write_transaction()
    trg = tr.create_node()
    tr.create_edge(src, trg, "edge")
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertEqual(len(result), 1)

  def test_create_edge_multi_transaction_trg(self):
    tr = self.memory.create_write_transaction()
    trg = tr.create_node("trg")
    result = tr.run()

    trg = result["trg"]

    self.assertIsNotNone(result)
    self.assertTrue(isinstance(trg, int))

    tr = self.memory.create_write_transaction()
    src = tr.create_node()
    tr.create_edge(src, trg, "edge")
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertEqual(len(result), 1)

  def test_edge_to_edge(self):
    tr = self.memory.create_write_transaction()
    attr = tr.create_node("attr")
    src = tr.create_node("src")
    trg = tr.create_node("trg")
    edge = tr.create_edge(src, trg, "edge")
    
    tr.create_edge(attr, edge, "edge_attr")
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertEqual(len(result), 5)