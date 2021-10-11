import unittest

from sc.types import *

class TestTypes(unittest.TestCase):

  def test_invalid_arc(self):
    self.assertRaises(TypeError, Type, Type.ARC | Type.NODE)
    self.assertRaises(TypeError, Type, Type.ARC | Type.NODE_TUPLE)
    self.assertRaises(TypeError, Type, Type.ARC | Type.EDGE)
    self.assertRaises(TypeError, Type, Type.ARC | Type.LINK)

    self.assertRaises(TypeError, Type, Type.ARC | Type.ARC_FUZ | Type.ARC_NEG)
    self.assertRaises(TypeError, Type, Type.ARC | Type.CONST | Type.VAR)
    self.assertRaises(TypeError, Type, Type.ARC | Type.ARC_PERM | Type.ARC_TEMP)

  def test_invalid_node(self):
    self.assertRaises(TypeError, Type, Type.NODE | Type.LINK)
    self.assertRaises(TypeError, Type, Type.NODE | Type.NODE_ABSTRACT | Type.NODE_CLASS)
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
    self.assertRaises(TypeError, Type, Type.ARC_MEMBER | Type.ARC_FUZ | Type.ARC_NEG)
    self.assertRaises(TypeError, Type, Type.ARC_MEMBER | Type.ARC_PERM | Type.ARC_TEMP)
    self.assertRaises(TypeError, Type, Type.ARC_MEMBER | Type.CONST | Type.VAR)

  def test_invalid_flags_common(self):
    self.assertRaises(TypeError, Type, Type.ARC_MEMBER | Type.ARC_PERM | Type.ARC_TEMP)
    self.assertRaises(TypeError, Type, Type.ARC_MEMBER | Type.ARC_POS | Type.ARC_NEG)
    self.assertRaises(TypeError, Type, Type.NODE | Type.CONST | Type.VAR)
    self.assertRaises(TypeError, Type, Type.CONST | Type.ARC_FUZ)

  def test_valid_flags_common(self):
    t = Unknown()

    self.assertFalse(t.isArc())
    self.assertFalse(t.isArcMember())
    self.assertFalse(t.isConnector())
    self.assertFalse(t.isConst())
    self.assertFalse(t.isEdge())
    self.assertFalse(t.isLink())
    self.assertFalse(t.isNode())
    self.assertFalse(t.isVar())

    t = UnknownConst()

    self.assertTrue(t.isConst())
    self.assertFalse(t.isVar())
    self.assertFalse(t.isConnector())
    self.assertFalse(t.isLink())
    self.assertFalse(t.isNode())

    t = UnknownVar()

    self.assertTrue(t.isVar())
    self.assertFalse(t.isConst())
    self.assertFalse(t.isConnector())
    self.assertFalse(t.isLink())
    self.assertFalse(t.isNode())

  def test_valid_node(self):

    tests = [
      (Node, False, 0),
      (NodeConst, True, 0),
      (NodeConstAbstract, True, Type.NODE_ABSTRACT),
      (NodeConstClass, True, Type.NODE_CLASS),
      (NodeConstMaterial, True, Type.NODE_MATERIAL),
      (NodeConstNoRole, True, Type.NODE_NO_ROLE),
      (NodeConstRole, True, Type.NODE_ROLE),
      (NodeConstStruct, True, Type.NODE_STRUCT),
      (NodeConstTuple, True, Type.NODE_TUPLE),
      (NodeVar, False, 0),
      (NodeVarAbstract, False, Type.NODE_ABSTRACT),
      (NodeVarClass, False, Type.NODE_CLASS),
      (NodeVarMaterial, False, Type.NODE_MATERIAL),
      (NodeVarNoRole, False, Type.NODE_NO_ROLE),
      (NodeVarRole, False, Type.NODE_ROLE),
      (NodeVarStruct, False, Type.NODE_STRUCT),
      (NodeVarTuple, False, Type.NODE_TUPLE),
    ]

    for test in tests:
      func, is_const, flag = test

      t = func()
      self.assertTrue(t.isNode(), str(func))
      self.assertEqual(t.isConst(), is_const, str(func))
      self.assertFalse(t.isLink(), str(func))
      self.assertFalse(t.isConnector(), str(func))

      if flag != 0:
        self.assertTrue(t.hasFlag(flag), str(func))

  def test_valid_links(self):

    tests = [
      (Link, False),
      (LinkConst, True),
      (LinkVar, False),
    ]

    for test in tests:
      func, is_const = test

      t = func()
      self.assertTrue(t.isLink(), str(func))
      self.assertFalse(t.isNode(), str(func))
      self.assertEqual(t.isConst(), is_const, str(func))
      self.assertFalse(t.isConnector(), str(func))

  def test_valid_edges(self):

    tests = [
      (Edge, False),
      (EdgeConst, True),
      (EdgeVar, False),
    ]

    for test in tests:
      func, is_const = test

      t = func()
      self.assertTrue(t.isEdge(), str(func))
      self.assertTrue(t.isConnector(), str(func))
      self.assertFalse(t.isArc(), str(func))
      self.assertFalse(t.isArcMember(), str(func))
      self.assertFalse(t.isNode(), str(func))
      self.assertEqual(t.isConst(), is_const, str(func))
      self.assertFalse(t.isLink(), str(func))

  def test_valid_arcs(self):

    tests = [
      (Arc, False),
      (ArcConst, True),
      (ArcVar, False),
    ]

    for test in tests:
      func, is_const = test

      t = func()
      self.assertTrue(t.isArc(), str(func))
      self.assertTrue(t.isConnector(), str(func))
      self.assertFalse(t.isArcMember(), str(func))
      self.assertFalse(t.isEdge(), str(func))
      self.assertFalse(t.isNode(), str(func))
      self.assertEqual(t.isConst(), is_const, str(func))
      self.assertFalse(t.isLink(), str(func))

