import unittest

from sc.scs.parser import SCsParser
from sc.scs.types import Arc, Edge, Element, Link, Node


class TestSCsLink(unittest.TestCase):

    def test_link_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> [value];;"))
        self.assertEqual(len(parser.triples), 1)

        _, _, link = parser.triples[0]
        self.assertIsInstance(link, Link)
        self.assertEqual(link.type, Link.Type.STRING)
        self.assertEqual(link.value, "value")

    def test_url_smoke(self):
        parser = SCsParser()

        self.assertTrue(parser.parse("a -> \"url://value\";;"))
        self.assertEqual(len(parser.triples), 1)

        _, _, link = parser.triples[0]
        self.assertIsInstance(link, Link)
        self.assertEqual(link.type, Link.Type.URL)
        self.assertEqual(link.value, "url://value")
