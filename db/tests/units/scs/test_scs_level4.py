import unittest

from sc.scs.parser import SCsParser
from sc.scs.types import *


class TestSCsLevel4(unittest.TestCase):

    def test_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> b: c; d;;"))
        self.assertEqual(len(parser.triples), 4)

        src, _, trg = parser.triples[0]
        self.assertEqual(src.name, "a")
        self.assertEqual(trg.name, "c")

        src, _, trg = parser.triples[1]
        self.assertEqual(src.name, "b")
        self.assertIsInstance(trg, Arc)

        src, _, trg = parser.triples[2]
        self.assertEqual(src.name, "a")
        self.assertEqual(trg.name, "d")

        src, _, trg = parser.triples[3]
        self.assertEqual(src.name, "b")
        self.assertIsInstance(trg, Arc)

    def test_complex(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> b: c; <- d: e: f;;"))
        self.assertEqual(len(parser.triples), 5)

        src, _, trg = parser.triples[0]
        self.assertEqual(src.name, "a")
        self.assertEqual(trg.name, "c")

        src, _, trg = parser.triples[1]
        self.assertEqual(src.name, "b")
        self.assertIsInstance(trg, Arc)

        src, _, trg = parser.triples[2]
        self.assertEqual(src.name, "f")
        self.assertEqual(trg.name, "a")

        src, _, trg = parser.triples[3]
        self.assertEqual(src.name, "d")
        self.assertIsInstance(trg, Arc)

        src, _, trg = parser.triples[4]
        self.assertEqual(src.name, "e")
        self.assertIsInstance(trg, Arc)
