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
