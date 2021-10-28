import unittest

from sc.scs.types import *
from sc.scs.parser import SCsParser


class TestSCsParserLevel3(unittest.TestCase):

    def test_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> c: _b:: d;;"))
        self.assertEqual(len(parser.triples), 3)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "a")
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "d")

        src, edge, trg = parser.triples[1]
        self.assertEqual(src.name, "c")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Arc)

        src, edge, trg = parser.triples[2]
        self.assertEqual(src.name, "_b")
        self.assertEqual(edge.connector, "_->")
        self.assertIsInstance(trg, Arc)

    def test_complex(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("(a _<- f: d) -/> (c ~> b:: d);;"))
        self.assertEqual(len(parser.triples), 5)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "d")
        self.assertEqual(edge.connector, "_->")
        self.assertEqual(trg.name, "a")

        src, edge, trg = parser.triples[1]
        self.assertEqual(src.name, "f")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Arc)
        self.assertEqual(trg.connector, "_->")

        src, edge, trg = parser.triples[2]
        self.assertEqual(src.name, "c")
        self.assertEqual(edge.connector, "~>")
        self.assertEqual(trg.name, "d")

        src, edge, trg = parser.triples[3]
        self.assertEqual(src.name, "b")
        self.assertEqual(edge.connector, "_->")
        self.assertIsInstance(trg, Arc)
        self.assertEqual(trg.connector, "~>")

        src, edge, trg = parser.triples[4]
        self.assertIsInstance(src, Arc)
        self.assertEqual(edge.connector, "-/>")
        self.assertIsInstance(trg, Arc)
