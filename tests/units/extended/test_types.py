import types
import unittest

from sc.types import *


class TestTypes(unittest.TestCase):

    def test_invalid_arc(self):
        self.assertRaises(TypeError, Type,
                          typeSem=TypeSemantic.ARC,
                          typeNode=TypeNode.TUPLE)

    def test_invalid_node(self):
        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.NODE,
                          typeArcPerm=TypeArcPerm.PERM)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.NODE,
                          typeArcPos=TypeArcPos.FUZ)

    def test_invalid_edge(self):

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.EDGE,
                          typeArcPerm=TypeArcPerm.PERM)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.EDGE,
                          typeArcPos=TypeArcPos.POS)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.EDGE,
                          typeNode=TypeNode.CLASS)

    def test_invalid_link(self):
        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.LINK,
                          typeArcPerm=TypeArcPerm.PERM)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.LINK,
                          typeArcPos=TypeArcPos.POS)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.LINK,
                          typeNode=TypeNode.ABSTRACT)

    def test_invalid_arc_member(self):
        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.ARC_MEMBER,
                          typeConst=TypeConst.CONST,
                          typeArcPos=TypeArcPos.UNKNOWN,
                          typeArcPerm=TypeArcPerm.PERM)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.ARC_MEMBER,
                          typeConst=TypeConst.CONST,
                          typeArcPos=TypeArcPos.FUZ,
                          typeArcPerm=TypeArcPerm.PERM)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.ARC_MEMBER,
                          typeConst=TypeConst.CONST,
                          typeArcPos=TypeArcPos.NEG,
                          typeArcPerm=TypeArcPerm.PERM)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.ARC_MEMBER,
                          typeConst=TypeConst.CONST,
                          typeArcPerm=TypeArcPerm.TEMP,
                          typeArcPos=TypeArcPos.POS)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.ARC_MEMBER,
                          typeConst=TypeConst.CONST,
                          typeArcPerm=TypeArcPerm.UNKNOWN,
                          typeArcPos=TypeArcPos.POS)

        self.assertRaises(TypeError,
                          Type,
                          typeSem=TypeSemantic.ARC_MEMBER,
                          typeConst=TypeConst.VAR,
                          typeArcPerm=TypeArcPerm.PERM,
                          typeArcPos=TypeArcPos.POS)

    def test_valid(self):
        t = Type.UNKNOWN()

        self.assertFalse(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertFalse(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertFalse(t.isNode())
        self.assertFalse(t.isVar())

        t = Type.NODE(typeConst=TypeConst.CONST)

        self.assertFalse(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertFalse(t.isConnector())
        self.assertTrue(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertTrue(t.isNode())
        self.assertFalse(t.isVar())

        t = Type.LINK(typeConst=TypeConst.VAR)

        self.assertFalse(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertFalse(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertTrue(t.isLink())
        self.assertFalse(t.isNode())
        self.assertTrue(t.isVar())

        t = Type.ARC()

        self.assertTrue(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertTrue(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertFalse(t.isNode())
        self.assertFalse(t.isVar())

        t = Type.ARC_MEMBER()

        self.assertFalse(t.isArc())
        self.assertTrue(t.isArcMember())
        self.assertTrue(t.isConnector())
        self.assertTrue(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertFalse(t.isNode())
        self.assertFalse(t.isVar())

        t = Type.EDGE()

        self.assertFalse(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertTrue(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertTrue(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertFalse(t.isNode())
        self.assertFalse(t.isVar())
