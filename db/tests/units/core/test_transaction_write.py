from unittest import result
import unittest
from sc.core.types import ArcType, LinkType, NodeType, TypeArcPerm, TypeArcPos, TypeConst, TypeNodeStruct
from tests.memory_case import MemoryTestCase

from sc.core.element import Element, Link
from sc.core.transaction import *
from sc.core.keywords import Labels


NodeConst = NodeType(const=TypeConst.CONST)
LinkConst = LinkType(const=TypeConst.CONST)
ArcMemberConstPosPerm = ArcType(
    const=TypeConst.CONST,
    arc_pos=TypeArcPos.POS,
    arc_perm=TypeArcPerm.PERM,
    is_member=True)


class TestCommon(MemoryTestCase):

    def test_duplicate_alias(self):
        tr = TransactionWrite(self.memory.driver)
        tr.create_node(NodeConst, alias="alias")
        self.assertRaises(KeyError, tr.create_node, NodeConst, "alias")

    def test_no_aliases(self):
        tr = TransactionWrite(self.memory.driver)
        tr.create_node(NodeConst)
        tr.create_node(NodeConst)
        result = tr.run()

        self.assertIsNotNone(result)

    def test_created_results(self):

        tr = TransactionWrite(self.memory.driver)
        node = tr.create_node(NodeConst)
        link = tr.create_link_with_content(
            LinkConst, content="test_content", is_url=False)
        arc = tr.create_edge(node, link, ArcMemberConstPosPerm)

        result = tr.run()

        node = result[node]
        self.assertIsNotNone(node)
        self.assertTrue(node.type.is_node())
        self.assertTrue(node.type.is_const())
        self.assertIsInstance(node.type, NodeType)

        link = result[link]
        self.assertIsNotNone(link)
        self.assertTrue(link.type.is_link())
        self.assertTrue(link.type.is_const())
        self.assertIsInstance(link.type, LinkType)

        arc = result[arc]
        self.assertIsNotNone(arc)
        self.assertTrue(arc.type.is_arc())
        self.assertTrue(arc.type.is_const())
        self.assertTrue(arc.type.is_member)
        self.assertIsInstance(arc.type, ArcType)


class TestNodes(MemoryTestCase):

    def create_node_dummy(self):
        tr = TransactionWrite(self.memory.driver)
        name = tr.create_node(NodeConst, alias="alias")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result.values), 1)
        self.assertTrue("alias" in result.values)
        self.assertEqual(name, "alias")

    def test_create_nodes(self):
        tr = TransactionWrite(self.memory.driver)
        tr.create_node(NodeConst, alias="alias")
        tr.create_node(NodeConst, alias="alias2")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result.values), 2)
        self.assertTrue("alias" in result.values)
        self.assertTrue("alias2" in result.values)

    def test_create_nodes_large(self):
        nodes_num = 1000
        tr = TransactionWrite(self.memory.driver)
        for i in range(nodes_num):
            tr.create_node(NodeConst, alias="alias_{}".format(i))

        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result.values), nodes_num)

        for i in range(nodes_num):
            self.assertTrue("alias_{}".format(i) in result.values)


class TestEdges(MemoryTestCase):

    def test_create_edge_dummy(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node(NodeConst)
        trg = tr.create_node(NodeConst)
        tr.create_edge(src, trg, ArcMemberConstPosPerm, "edge")

        result = tr.run()
        self.assertIsNotNone(result)
        self.assertEqual(len(result.values.keys()), 3)
        self.assertTrue("edge" in result.values)

    def test_create_edge_multi_transaction(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node(NodeConst, alias="src")
        trg = tr.create_node(NodeConst, alias="trg")
        result = tr.run()

        self.assertIsNotNone(result)

        src = result["src"]
        trg = result["trg"]

        self.assertTrue(isinstance(src, Element))
        self.assertTrue(isinstance(trg, Element))

        tr = TransactionWrite(self.memory.driver)
        tr.create_edge(src, trg, ArcMemberConstPosPerm, "edge")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

    def test_create_edge_multi_transaction_src(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node(NodeConst, alias="src")
        result = tr.run()

        src = result["src"]

        self.assertIsNotNone(result)
        self.assertTrue(isinstance(src, Element))
        self.assertEqual(len(result), 1)

        tr = TransactionWrite(self.memory.driver)
        trg = tr.create_node(NodeConst)
        tr.create_edge(src, trg, ArcMemberConstPosPerm, "edge")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

    def test_create_edge_multi_transaction_trg(self):
        tr = TransactionWrite(self.memory.driver)
        trg = tr.create_node(NodeConst, alias="trg")
        result = tr.run()

        trg = result["trg"]

        self.assertIsNotNone(result)
        self.assertTrue(isinstance(trg, Element))
        self.assertEqual(len(result), 1)

        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node(NodeConst)
        tr.create_edge(src, trg, ArcMemberConstPosPerm, "edge")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

    def test_edge_to_edge(self):

        tr = TransactionWrite(self.memory.driver)
        attr = tr.create_node(NodeConst, alias="attr")
        src = tr.create_node(NodeConst, alias="src")
        trg = tr.create_node(NodeConst, alias="trg")
        edge = tr.create_edge(src, trg, ArcMemberConstPosPerm, alias="edge")

        tr.create_edge(attr, edge, ArcMemberConstPosPerm, alias="edge_attr")
        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 5)


class TestLinks(MemoryTestCase):

    def test_links(self):
        tr = TransactionWrite(self.memory.driver)
        link_int = tr.create_link_with_content(
            LinkConst,
            alias="link_int",
            content=5)
        link_float = tr.create_link_with_content(
            LinkConst,
            alias="link_float",
            content=7.89)
        link_str = tr.create_link_with_content(
            LinkConst,
            alias="link_str",
            content="string_content")
        link_url = tr.create_link_with_content(
            LinkConst,
            alias="link_url",
            content="http://test.test")

        result = tr.run()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertIsNotNone(result[link_int])
        self.assertIsNotNone(result[link_float])
        self.assertIsNotNone(result[link_str])
        self.assertIsNotNone(result[link_url])
