import unittest

from sc.types import *


class TestTypes(unittest.TestCase):

    def test_invalid_arc(self):
        self.assertRaises(TypeError, Type, Type.ARC | Type.NODE)
        self.assertRaises(TypeError, Type, Type.ARC | Type.NODE_TUPLE)
        self.assertRaises(TypeError, Type, Type.ARC | Type.EDGE)
        self.assertRaises(TypeError, Type, Type.ARC | Type.LINK)

        self.assertRaises(TypeError, Type, Type.ARC |
                          Type.ARC_FUZ | Type.ARC_NEG)
        self.assertRaises(TypeError, Type, Type.ARC | Type.CONST | Type.VAR)
        self.assertRaises(TypeError, Type, Type.ARC |
                          Type.ARC_PERM | Type.ARC_TEMP)

    def test_invalid_node(self):
        self.assertRaises(TypeError, Type, Type.NODE | Type.LINK)
        self.assertRaises(TypeError, Type, Type.NODE |
                          Type.NODE_ABSTRACT | Type.NODE_CLASS)
        self.assertRaises(TypeError, Type, Type.NODE | Type.ARC_FUZ)
        self.assertRaises(TypeError, Type, Type.NODE | Type.ARC_PERM)
        self.assertRaises(TypeError, Type, Type.NODE | Type.CONST | Type.VAR)

    def test_invalid_edge(self):
        self.assertRaises(TypeError, Type, Type.EDGE | Type.ARC_FUZ)
        self.assertRaises(TypeError, Type, Type.EDGE | Type.ARC_PERM)
        self.assertRaises(TypeError, Type, Type.EDGE | Type.CONST | Type.VAR)
        self.assertRaises(TypeError, Type, Type.EDGE | Type.NODE_ABSTRACT)

    def test_invalid_link(self):
        self.assertRaises(TypeError, Type, Type.LINK | Type.ARC_PERM)
        self.assertRaises(TypeError, Type, Type.LINK | Type.NODE_ABSTRACT)
        self.assertRaises(TypeError, Type, Type.LINK | Type.NODE)
        self.assertRaises(TypeError, Type, Type.LINK | Type.ARC_FUZ)
        self.assertRaises(TypeError, Type, Type.LINK | Type.CONST | Type.VAR)

    def test_invalid_arc_member(self):
        self.assertRaises(TypeError, Type, Type.ARC_MEMBER | Type.EDGE)
        self.assertRaises(TypeError, Type, Type.ARC_MEMBER |
                          Type.ARC_FUZ | Type.ARC_NEG)
        self.assertRaises(TypeError, Type, Type.ARC_MEMBER |
                          Type.ARC_PERM | Type.ARC_TEMP)
        self.assertRaises(TypeError, Type, Type.ARC_MEMBER |
                          Type.CONST | Type.VAR)
        self.assertRaises(TypeError, Type, Type.ARC | Type.ARC_MEMBER)

    def test_invalid_flags_common(self):
        self.assertRaises(TypeError, Type, Type.ARC_MEMBER |
                          Type.ARC_PERM | Type.ARC_TEMP)
        self.assertRaises(TypeError, Type, Type.ARC_MEMBER |
                          Type.ARC_POS | Type.ARC_NEG)
        self.assertRaises(TypeError, Type, Type.NODE | Type.CONST | Type.VAR)
        self.assertRaises(TypeError, Type, Type.CONST | Type.ARC_FUZ)

    def test_valid_flags_common(self):
        t = Type(Type.UNKNOWN)

        self.assertFalse(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertFalse(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertFalse(t.isNode())
        self.assertFalse(t.isVar())

        t = Type(Type.NODE | Type.CONST)

        self.assertFalse(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertFalse(t.isConnector())
        self.assertTrue(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertTrue(t.isNode())
        self.assertFalse(t.isVar())

        t = Type(Type.LINK | Type.VAR)

        self.assertFalse(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertFalse(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertTrue(t.isLink())
        self.assertFalse(t.isNode())
        self.assertTrue(t.isVar())

        t = Type(Type.ARC)

        self.assertTrue(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertTrue(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertFalse(t.isNode())
        self.assertFalse(t.isVar())

        t = Type(Type.ARC_MEMBER)

        self.assertFalse(t.isArc())
        self.assertTrue(t.isArcMember())
        self.assertTrue(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertFalse(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertFalse(t.isNode())
        self.assertFalse(t.isVar())

        t = Type(Type.EDGE)

        self.assertFalse(t.isArc())
        self.assertFalse(t.isArcMember())
        self.assertTrue(t.isConnector())
        self.assertFalse(t.isConst())
        self.assertTrue(t.isEdge())
        self.assertFalse(t.isLink())
        self.assertFalse(t.isNode())
        self.assertFalse(t.isVar())
