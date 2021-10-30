from ast import parse
import unittest

from sc.scs.parser import SCsParser
from sc.scs.types import *


class TestSCsLevel6(unittest.TestCase):

    def test_smoke(self):
        tests = ["z -> [**];;",
                 "x -> [test*];;",
                 "@a = [\\[* r-> b;; *\\]];;",
                 "@alias = u;; @alias -> [* x -> [* y -> z;; *];; *];;",
                 "y <= nrel_main_idtf: [y*];;",
                 "a -> [* z -> [begin*];; *];;",
                 "a -> [* b -> c;; *];;"]
        for t in tests:
            parser = SCsParser()
            self.assertTrue(parser.parse(t))

    def test_set(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("@set = { a; b: c; d: e: f };;"))
        self.assertEqual(len(parser.triples), 6)

        common_src = parser.triples[0][0]

        src, edge, trg = parser.triples[0]
        self.assertIsInstance(src, Node)
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "a")

        src, edge, trg = parser.triples[1]
        self.assertIsInstance(src, Node)
        self.assertEqual(src.name, common_src.name)
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "c")

        src, edge, trg = parser.triples[2]
        self.assertEqual(src.name, "b")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Arc)

        src, edge, trg = parser.triples[3]
        self.assertIsInstance(src, Node)
        self.assertEqual(src.name, common_src.name)
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "f")

        src, edge, trg = parser.triples[4]
        self.assertEqual(src.name, "d")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Arc)

        src, edge, trg = parser.triples[5]
        self.assertEqual(src.name, "e")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Arc)

    def test_set_recursive(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("@set = { a; {b} };;"))
        self.assertEqual(len(parser.triples), 3)

        src, edge, trg = parser.triples[0]
        self.assertIsInstance(src, Node)
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Node)

        src, edge, trg = parser.triples[1]
        self.assertIsInstance(src, Node)
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "b")

        prev_src = src

        src, edge, trg = parser.triples[2]
        self.assertEqual(prev_src.name, trg.name)

        self.assertIsInstance(src, Node)
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Node)

    def test_content_empty(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> [];;"))
        self.assertEqual(len(parser.triples), 1)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "a")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Link)
        self.assertEqual(trg.value, "")
        self.assertTrue(trg.is_const())

    def test_content_simple(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> [simple];;"))
        self.assertEqual(len(parser.triples), 1)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "a")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Link)
        self.assertEqual(trg.value, "simple")
        self.assertTrue(trg.is_const())

    def test_content_var(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> _[simple];;"))
        self.assertEqual(len(parser.triples), 1)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "a")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Link)
        self.assertEqual(trg.value, "simple")
        self.assertTrue(trg.is_var())

    def test_content_multiline(self):
        parser = SCsParser()

        self.assertTrue(parser.parse((
            "a -> [simple\n"
            " multiline];;")))
        self.assertEqual(len(parser.triples), 1)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "a")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Link)
        self.assertEqual(len(trg.value.split('\n')), 2)
        self.assertTrue(trg.is_const())

    def test_content_escaping(self):
        tests = [
            ("x -> _[\\[test\\]];;", "[test]"),
            ("x -> _[\\\\\\[test\\\\\\]];;", "\\[test\\]")
        ]

        for input, output in tests:
            parser = SCsParser()
            self.assertTrue(parser.parse(input))
            self.assertEqual(len(parser.triples), 1)

            _, _, link = parser.triples[0]
            self.assertIsInstance(link, Link)
            self.assertEqual(link.value, output)

    def test_content_error(self):
        tests = [
            "@alias = [;;",
            "x -> y (* -> name: [name ;;",
            ]

        for t in tests:
            parser = SCsParser()
            self.assertFalse(parser.parse(t))
            self.assertGreater(len(parser.errors), 0)

    def test_contour_empty(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("x -> [**];;"))
        self.assertEqual(len(parser.triples), 1)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "x")
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Node)

    def test_contour_simple(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("x -|> [* y _=> z;; *];;"))
        self.assertEqual(len(parser.triples), 5)

        src, edge, trg = parser.triples[0]
        self.assertEqual(src.name, "y")
        self.assertEqual(edge.connector, "_=>")
        self.assertEqual(trg.name, "z")

        _, edge, trg = parser.triples[1]
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "y")

        _, edge, trg = parser.triples[2]
        self.assertEqual(edge.connector, "->")
        self.assertIsInstance(trg, Edge)
        self.assertEqual(trg.connector, "_=>")

        _, edge, trg = parser.triples[3]
        self.assertEqual(edge.connector, "->")
        self.assertEqual(trg.name, "z")

        src, edge, trg = parser.triples[4]
        self.assertEqual(src.name, "x")
        self.assertEqual(edge.connector, "-|>")
        self.assertIsInstance(trg, Node)


    def test_countour_recursive(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("x ~|> [* y _=> [* k ~> z;; *];; *];;"))
        self.assertEqual(len(parser.triples), 9)

    def test_countour_with_content(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("x -> [* y _=> [test*];; *];;"))
        self.assertEqual(len(parser.triples), 5)

        _, edge, trg = parser.triples[0]
        self.assertIsInstance(trg, Link)
        self.assertEqual(trg.value, "test*")
        self.assertEqual(edge.connector, "_=>")

    def test_countour_error(self):
        tests = [
            "x -> [* y -> z *];;",
            "y -> [* z -> [* *];;",
            "x -> [* y -> z;; ];;",
        ]

        for t in tests:
            parser = SCsParser()
            self.assertFalse(parser.parse(t))
            self.assertEqual(len(parser.errors), 1)
