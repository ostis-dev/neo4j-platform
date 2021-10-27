import unittest

from sc.scs.types import *


class TestSCsElement(unittest.TestCase):

    def test_element_idtf(self):
        el = Element(Element.Kind.NODE, name="_idtf", ctx=None)
        self.assertTrue(el.is_var())

        el = Element(Element.Kind.NODE, name=".._idtf", ctx=None)
        self.assertTrue(el.is_var())

        el = Element(Element.Kind.NODE, name="._idtf", ctx=None)
        self.assertTrue(el.is_var())

        el = Element(Element.Kind.NODE, name="_idtf", ctx=None)
        self.assertTrue(el.is_var())

        el = Element(Element.Kind.NODE, name="...", ctx=None)
        self.assertTrue(el.is_const())

        el = Element(Element.Kind.NODE, name="..idtf", ctx=None)
        self.assertTrue(el.is_const())

        el = Element(Element.Kind.NODE, name=".idtf", ctx=None)
        self.assertTrue(el.is_const())

    def test_arc_reverse(self):
        arc = Arc('->', '', TokenContext(0, 0, ''))
        self.assertFalse(arc._reverse_if_back())

        arc.connector = '<-'
        self.assertTrue(arc._reverse_if_back())
        self.assertEqual(arc.connector, '->')

    def test_edge_reverse(self):
        edge = Edge('_=>', '', TokenContext(0, 0, ''))
        self.assertFalse(edge._reverse_if_back())

        edge.connector = '_<='
        self.assertTrue(edge._reverse_if_back())
        self.assertEqual(edge.connector, '_=>')
