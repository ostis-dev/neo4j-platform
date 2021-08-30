import sc
from tests.memory_case import MemoryTestCase

class TestConnect(MemoryTestCase):

  def test_create_nodes(self):
    tr = self.memory.create_write_transaction()
    tr.create_node("alias")
    tr.create_node("alias2")
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertTrue(len(result.values.keys()) == 2)
    self.assertTrue("alias" in result.values)
    self.assertTrue("alias2" in result.values)

  def test_create_nodes_large(self):
    nodes_num = 100
    tr = self.memory.create_write_transaction()
    for i in range(nodes_num):
      tr.create_node("alias_{}".format(i))
    result = tr.run()

    self.assertIsNotNone(result)
    self.assertTrue(len(result.values.keys()) == nodes_num)

    for i in range(nodes_num):
      self.assertTrue("alias_{}".format(i) in result.values)