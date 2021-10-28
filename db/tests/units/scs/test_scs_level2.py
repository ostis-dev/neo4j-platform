import unittest

from sc.scs.types import *
from sc.scs.parser import SCsParser


class TestSCsParserLevel2(unittest.TestCase):

    def test_reverse(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("b <- a;;"))
        self.assertEqual(len(parser.triples), 1)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "a")
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "b")

    def test_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> (b <- c);;"))
        self.assertEqual(len(parser.triples), 2)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "c")
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "b")

        src, edge, trg = parser.triples[1]
        self.assertEqual(src.name, "a")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Arc)

    def test_smoke_2(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("(c <- x) <- (b <> y);;"))
        self.assertEqual(len(parser.triples), 3)

        src, edge, trg = parser.triples[0]
        self.assertIsInstance(src, Node)
        self.assertEqual(src.name, "x")
        self.assertIsInstance(edge, Arc)
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Node)
        self.assertEqual(trg.name, "c")

        src, edge, trg = parser.triples[1]
        self.assertIsInstance(src, Node)
        self.assertEqual(src.name, "b")
        self.assertIsInstance(edge, Edge)
        self.assertEqual(edge.connector, "<>")
        self.assertIsInstance(trg, Node)
        self.assertEqual(trg.name, "y")

        src, edge, trg = parser.triples[2]
        self.assertIsInstance(src, Edge)
        self.assertIsInstance(edge, Arc)
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Arc)

    def test_unnamed(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> ...; -> ...;;"))
        self.assertEqual(len(parser.triples), 2)

        _, _, trg = parser.triples[0]
        self.assertIsInstance(trg, Node)

        _, _, trg = parser.triples[1]
        self.assertIsInstance(trg, Node)

    def test_invalid(self):
        tests = ["a -> (x -> (y -> z));;",
                 "a -> (x -> [content]);;",
                 "a -> (x -> [* y -> z ;; *]);;",
                 "a -> (x -> { y; z });;"]

        for t in tests:
            parser = SCsParser()
            self.assertFalse(parser.parse(t))
            self.assertGreater(len(parser.errors), 0)
