import unittest

from sc.scs.parser import SCsParser
from sc.scs.types import *


class TestSCsLevel5(unittest.TestCase):

    def test_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse((
            "set ~> attr:: item"
            "  (* -/> subitem;;"
            "     <= subitem2;; *);;")))

        self.assertEqual(len(parser.triples), 4)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "item")
        self.assertEqual(edge.connector, "-/>")
        self.assertEqual(trg.name, "subitem")

        src, edge, trg = parser.triples[1]
        self.assertEqual(src.name, "subitem2")
        self.assertEqual(edge.connector, "=>")
        self.assertEqual(trg.name, "item")

        src, edge, trg = parser.triples[2]
        self.assertEqual(src.name, "set")
        self.assertIsInstance(edge, Arc)
        self.assertEqual(trg.name, "item")

        src, edge, trg = parser.triples[3]
        self.assertEqual(src.name, "attr")
        self.assertEqual(edge.connector, "_->")
        self.assertIsInstance(trg, Arc)
