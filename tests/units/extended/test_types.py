import types
import unittest

from sc.types import *


class TestTypes(unittest.TestCase):

    def test_unknown(self):
        t = UnknownType()

        self.assertFalse(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isVar())

    def test_node(self):
        t = NodeType()

        self.assertEqual(t.kind, BaseType.Kind.NODE)
        self.assertEqual(t.typeConst, TypeConst.UNKNOWN)
        self.assertEqual(t.typeStruct, TypeNodeStruct.UNKNOWN)
        self.assertFalse(t.isConnector())

        t = NodeType(typeConst=TypeConst.CONST)

        self.assertTrue(t.isConst())
        self.assertFalse(t.isVar())

        t = NodeType(typeConst=TypeConst.VAR,
                     typeStruct=TypeNodeStruct.ABSTRACT)

        self.assertTrue(t.isVar())
        self.assertFalse(t.isConst())
        self.assertEqual(t.typeStruct, TypeNodeStruct.ABSTRACT)

    def test_link(self):
        t = LinkType()

        self.assertEqual(t.kind, BaseType.Kind.LINK)
        self.assertFalse(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isVar())

        t = LinkType(typeConst=TypeConst.CONST)

        self.assertTrue(t.isConst())
        self.assertFalse(t.isVar())

    def test_edge(self):

        t = EdgeType()

        self.assertEqual(t.kind, BaseType.Kind.EDGE)
        self.assertTrue(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isVar())

        t = EdgeType(typeConst=TypeConst.VAR)

        self.assertTrue(t.isVar())
        self.assertFalse(t.isConst())

    def test_arc(self):

        t = ArcType()

        self.assertEqual(t.kind, BaseType.Kind.ARC)
        self.assertTrue(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isVar())

        t = ArcType(typeConst=TypeConst.VAR,
                    typeArcPos=TypeArcPos.FUZ, typeArcPerm=TypeArcPerm.PERM)

        self.assertTrue(t.isVar())
        self.assertFalse(t.isConst())
        self.assertEqual(t.typeArcPerm, TypeArcPerm.PERM)
        self.assertEqual(t.typeArcPos, TypeArcPos.FUZ)
