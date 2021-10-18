import sc
import unittest


class TestConnect(unittest.TestCase):

    def test_connect_positive(self):
        try:
            memory = sc.Memory("config.ini")
            self.assertTrue(memory.client.has_db("neo4j"))
            memory.close()
        except:
            self.fail("Wasn't able to connect")

    def test_connect_non_exist_config(self):
        fail = False
        try:
            memory = sc.Memory("non_exist_config.ini")
            memory.close()
        except:
            fail = True

        self.assertTrue(fail, "Was not failed")
