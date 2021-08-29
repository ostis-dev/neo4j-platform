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