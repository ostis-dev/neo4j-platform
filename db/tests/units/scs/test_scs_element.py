import unittest

from sc.scs.element import *


class TestSCsElement(unittest.TestCase):

    def test_element_idtf(self):
        el = Element(Element.Kind.NODE, name="_idtf")
        self.assertTrue(el.is_var())

        el = Element(Element.Kind.NODE, name=".._idtf")
        self.assertTrue(el.is_var())

        el = Element(Element.Kind.NODE, name="._idtf")
        self.assertTrue(el.is_var())

        el = Element(Element.Kind.NODE, name="_idtf")
        self.assertTrue(el.is_var())

        el = Element(Element.Kind.NODE, name="...")
        self.assertTrue(el.is_const())

        el = Element(Element.Kind.NODE, name="..idtf")
        self.assertTrue(el.is_const())

        el = Element(Element.Kind.NODE, name=".idtf")
        self.assertTrue(el.is_const())
