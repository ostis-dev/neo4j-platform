import unittest

from sc.scs.types import *
from sc.scs.parser import SCsParser


class TestSCsParserLevel1(unittest.TestCase):

    def test_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("sc_node#a | sc_edge#e1 | sc_link#b;;"))
        self.assertEqual(len(parser.triples), 1)

        src, edge, trg = parser.triples[0]
        self.assertIsInstance(src, Node)
        self.assertIsInstance(edge, Edge)
        self.assertIsInstance(trg, Link)

    def test_types(self):
        parser = SCsParser()

        data = ("sc_node#a | sc_edge#e1 | sc_link#b;;"
                "sc_node#c | sc_arc#e2 | sc_node#d;;")

        self.assertTrue(parser.parse(data))

        self.assertEqual(len(parser.triples), 2)

        src, edge, trg = parser.triples[0]
        self.assertIsInstance(src, Node)
        self.assertIsInstance(edge, Edge)
        self.assertIsInstance(trg, Link)

        src, edge, trg = parser.triples[1]
        self.assertIsInstance(src, Node)
        self.assertIsInstance(edge, Arc)
        self.assertIsInstance(trg, Node)

    def test_no_type(self):
        parser = SCsParser()
        self.assertFalse(parser.parse("#a | sc_edge#e1 | #b;;"))

    def test_no_edge_type(self):
        parser = SCsParser()
        self.assertFalse(parser.parse("#a | #e1 | #b;;"))
