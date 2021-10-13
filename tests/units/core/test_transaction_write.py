from unittest import result
from tests.memory_case import MemoryTestCase

from sc import ElementID
from sc.core.transaction import *


class TestCommon(MemoryTestCase):

    def test_duplicate_alias(self):
        tr = TransactionWrite(self.memory.driver)
        tr.create_node("alias")
        self.assertRaises(KeyError, tr.create_node, "alias")

    def test_no_aliases(self):
        tr = TransactionWrite(self.memory.driver)
        tr.create_node()
        tr.create_node()
        result = tr.run()

        self.assertIsNotNone(result)


class TestNodes(MemoryTestCase):

    def create_node_dummy(self):
        tr = TransactionWrite(self.memory.driver)
        name = tr.create_node("alias")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result.values), 1)
        self.assertTrue("alias" in result.values)
        self.assertEqual(name, "alias")

    def test_create_nodes(self):
        tr = TransactionWrite(self.memory.driver)
        tr.create_node("alias")
        tr.create_node("alias2")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result.values), 2)
        self.assertTrue("alias" in result.values)
        self.assertTrue("alias2" in result.values)

    def test_create_nodes_large(self):
        nodes_num = 1000
        tr = TransactionWrite(self.memory.driver)
        for i in range(nodes_num):
            tr.create_node("alias_{}".format(i))
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result.values), nodes_num)

        for i in range(nodes_num):
            self.assertTrue("alias_{}".format(i) in result.values)


class TestEdges(MemoryTestCase):

    def test_create_edge_dummy(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node()
        trg = tr.create_node()
        tr.create_edge(src, trg, "sc_edge", "edge")

        result = tr.run()
        self.assertIsNotNone(result)
        self.assertEqual(len(result.values.keys()), 1)
        self.assertTrue("edge" in result.values)

    def test_create_edge_multi_transaction(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node("src")
        trg = tr.create_node("trg")
        result = tr.run()

        self.assertIsNotNone(result)

        src = result["src"]
        trg = result["trg"]

        self.assertTrue(isinstance(src, ElementID))
        self.assertTrue(isinstance(trg, ElementID))

        tr = TransactionWrite(self.memory.driver)
        tr.create_edge(src, trg, "sc_edge", "edge")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

    def test_create_edge_multi_transaction_src(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node("src")
        result = tr.run()

        src = result["src"]

        self.assertIsNotNone(result)
        self.assertTrue(isinstance(src, ElementID))

        tr = TransactionWrite(self.memory.driver)
        trg = tr.create_node()
        tr.create_edge(src, trg, "sc_edge", "edge")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

    def test_create_edge_multi_transaction_trg(self):
        tr = TransactionWrite(self.memory.driver)
        trg = tr.create_node("trg")
        result = tr.run()

        trg = result["trg"]

        self.assertIsNotNone(result)
        self.assertTrue(isinstance(trg, ElementID))

        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node()
        tr.create_edge(src, trg, "sc_edge", "edge")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

    def test_edge_to_edge(self):
        tr = TransactionWrite(self.memory.driver)
        attr = tr.create_node("attr")
        src = tr.create_node("src")
        trg = tr.create_node("trg")
        edge = tr.create_edge(src, trg, "sc_edge", "edge")

        tr.create_edge(attr, edge, "sc_edge", "edge_attr")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 5)

    def test_links(self):
        tr = TransactionWrite(self.memory.driver)
        link_int = tr.create_link_with_content("link_int", 5)
        link_float = tr.create_link_with_content("link_float", 7.89)
        link_str = tr.create_link_with_content("link_str", "string_content")
        link_url = tr.create_link_with_content("link_url", "http://test.test")

        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertIsNotNone(result[link_int])
        self.assertIsNotNone(result[link_float])
        self.assertIsNotNone(result[link_str])
        self.assertIsNotNone(result[link_url])
