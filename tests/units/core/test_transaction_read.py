from unittest import result
from sc.core.element import Arc, Node
from sc.core.transaction.write import TransactionWrite
from sc.core.types import ArcType, NodeType, TypeArcPerm, TypeArcPos, TypeConst
from tests.memory_case import MemoryTestCase

from sc.core.transaction.read import *
from sc.core.keywords import Labels

NodeConst = NodeType(const=TypeConst.CONST)
ArcMemberConstPosPerm = ArcType(
    const=TypeConst.CONST,
    arc_pos=TypeArcPos.POS,
    arc_perm=TypeArcPerm.PERM,
    is_member=True)


class TestFindTemplate(MemoryTestCase):

    def test_find_triple(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node(NodeConst, alias="src")
        trg = tr.create_node(NodeConst, alias="trg")
        edge = tr.create_edge(src, trg, ArcMemberConstPosPerm, "edge")
        result = tr.run()

        self.assertEqual(len(result), 3)
        src = result[src]
        trg = result[trg]
        edge = result[edge]

        tr = TransactionRead(self.memory.driver)
        _src, _edge, _trg = tr.triple_faa(
            FixedParameter(src, "src"),
            AssignParameter(ArcMemberConstPosPerm, "edge"),
            AssignParameter(None, "trg"))
        result = tr.run()

        self.assertEqual(len(result), 1)
        items = result[0]

        self.assertEqual(items[_src], src)
        self.assertEqual(items[_trg], trg)
        self.assertEqual(items[_edge], edge)

    def test_find_constr_5(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node(NodeConst, alias="src")
        trg = tr.create_node(NodeConst, alias="trg")
        attr = tr.create_node(NodeConst, alias="attr")

        edge = tr.create_edge(src, trg, ArcMemberConstPosPerm, "edge")
        attr_edge = tr.create_edge(
            attr, edge, ArcMemberConstPosPerm, "attr_edge")

        result = tr.run()
        self.assertEqual(len(result), 5)
        src = result[src]
        trg = result[trg]
        attr = result[attr]
        edge = result[edge]
        attr_edge = result[attr_edge]

        tr = TransactionRead(self.memory.driver)
        _src, _edge, _trg = tr.triple_faf(
            FixedParameter(src, "src"),
            AssignParameter(ArcMemberConstPosPerm, "edge"),
            FixedParameter(trg, "trg"))
        _attr, _attr_edge, _ = tr.triple_faf(
            FixedParameter(attr, "attr"),
            AssignParameter(ArcMemberConstPosPerm, "attr_edge"),
            _edge)

        result = tr.run()

        self.assertEqual(len(result), 1)

        items = result[0]
        self.assertEqual(items[_src], src)
        self.assertEqual(items[_trg], trg)
        self.assertEqual(items[_edge], edge)
        self.assertEqual(items[_attr], attr)
        self.assertEqual(items[_attr_edge], attr_edge)

    def test_find_constr_5_edge_first(self):
        tr = TransactionWrite(self.memory.driver)
        src = tr.create_node(NodeConst, alias="src")
        trg = tr.create_node(NodeConst, alias="trg")
        attr = tr.create_node(NodeConst, alias="attr")

        edge = tr.create_edge(src, trg, ArcMemberConstPosPerm, "edge")
        attr_edge = tr.create_edge(
            attr, edge, ArcMemberConstPosPerm, "attr_edge")

        result = tr.run()
        self.assertEqual(len(result), 5)
        src = result[src]
        trg = result[trg]
        attr = result[attr]
        edge = result[edge]
        attr_edge = result[attr_edge]

        tr = TransactionRead(self.memory.driver)
        _src, _edge, _trg = tr.triple_afa(
            AssignParameter(None, "src"),
            FixedParameter(edge, "edge"),
            AssignParameter(None, "trg"))
        _attr, _attr_edge, _ = tr.triple_faf(
            FixedParameter(attr, "attr"),
            AssignParameter(ArcMemberConstPosPerm, "attr_edge"),
            _edge)

        result = tr.run()

        self.assertEqual(len(result), 1)

        items = result[0]
        self.assertEqual(items[_src], src)
        self.assertEqual(items[_trg], trg)
        self.assertEqual(items[_edge], edge)
        self.assertEqual(items[_attr], attr)
        self.assertEqual(items[_attr_edge], attr_edge)
