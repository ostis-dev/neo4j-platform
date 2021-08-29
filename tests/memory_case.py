import unittest

import sc

class MemoryTestCase(unittest.TestCase):
  def setUp(self):
    self.memory = sc.Memory("config.ini")

  def tearDown(self):
    self.memory.close()