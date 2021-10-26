import unittest

from sc.scs.parser import SCsParser
from sc.scs.types import Arc, Edge, Element, Link, Node


class TestSCsAlias(unittest.TestCase):

    def test_edge_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("@alias = (x -> y);;"))
        self.assertEqual(len(parser.triples), 1)

    def test_contour_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse(
            ("@alias = _[];;"
             "x -> [* @alias2 = y;;"
             "       @alias _~> @alias2;;"
             "*];;")))

        self.assertEqual(len(parser.triples), 5)

    def test_usage(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("@alias = [];; x ~> @alias;;"))
        self.assertEqual(len(parser.triples), 1)
        self.assertFalse(parser.has_warnings())

        src, _, trg = parser.triples[0]

        self.assertIsInstance(src, Node)
        self.assertIsInstance(trg, Link)

    def test_not_defined(self):
        parser = SCsParser()

        self.assertFalse(parser.parse("x -> @alias;;"))
        self.assertEqual(len(parser.errors), 1)
        self.assertFalse(parser.has_warnings())

    def test_reassign_warning(self):
        parser = SCsParser()

        self.assertTrue(parser.parse(
            ("@alias = (x -> y);;"
             "@alias = (z -> y);;")))
        self.assertEqual(len(parser.triples), 2)
        self.assertEqual(len(parser.warnings), 1)

    def test_reassign(self):
        parser = SCsParser()

        self.assertTrue(parser.parse(
            ("@alias = x;;"
             "y -> @alias;;"
             "@alias = z;;"
             "@alias -> c;;")))

        self.assertEqual(len(parser.triples), 2)

        src, _, _ = parser.triples[1]
        self.assertEqual(src.name, "z")

    def test_assign_alias_to_alias(self):
        parser = SCsParser()

        self.assertTrue(parser.parse(
            ("@alias1 = x;;"
             "@alias1 <- sc_node_tuple;;"
             "@alias2 = @alias1;;"
             "_y -|> @alias2;;")))

        self.assertEqual(len(parser.triples), 1)
        self.assertFalse(parser.has_warnings())

        _, _, trg = parser.triples[0]
        self.assertEqual(trg.name, "x")
