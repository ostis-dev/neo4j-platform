import unittest

from sc import SCsParser


class TestSCsParser(unittest.TestCase):

    def test_smoke(self):
        parser = SCsParser()
        self.assertTrue(parser.parse("x -> y;;"))

    def test_smoke_error(self):
        parser = SCsParser()
        self.assertFalse(parser.parse("x -> y;"))
        self.assertEqual(len(parser.errors), 1)

    def test_comments(self):
        parser = SCsParser()
        self.assertTrue(parser.parse((
            "//Level1\n"
            "a -> b;;/* example */\n"
            "c <> d;;"
        )))
        self.assertEqual(len(parser.triples), 2)

    def test_links(self):
        parser = SCsParser()
        self.assertTrue(parser.parse((
            "a -> \"file://data.txt\";;"
            "b -> [x];;"
            "c -> _[];;"
            "d -> [];;"
        )))
        self.assertEqual(len(parser.triples), 4)

    def test_type_no_error(self):
        parser = SCsParser()
        self.assertTrue(parser.parse((
            "a <- sc_node_abstract;;"
            "a <- sc_node_role_relation;;"
        )))
        self.assertFalse(parser.has_errors())
        self.assertEqual(len(parser.triples), 2)
