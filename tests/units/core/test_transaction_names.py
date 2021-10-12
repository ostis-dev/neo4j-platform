from unittest import result
from tests.memory_case import MemoryTestCase

from sc.core.transaction.names import TransactionNamesWrite


class TestNames(MemoryTestCase):

    def test_set_system_identifer_dummy(self):
        tr = self.memory.create_write_transaction()
        node = tr.create_node("node")
        node2 = tr.create_node("node2")
        result = tr.run()

        self.assertEqual(len(result), 2)

        node = result[node]
        node2 = result[node2]

        tr = self.memory.create_name_write_transaction()
        tr.set_system_identifier(node, "node_sys_idtf")
        tr.set_system_identifier(node2, "node_sys_idtf2")
        result = tr.run()

        self.assertIsNotNone(result)

    def test_replace_system_identifer_dummy(self):
        tr = self.memory.create_write_transaction()
        node = tr.create_node("node")
        result = tr.run()

        self.assertEqual(len(result), 1)

        node = result[node]

        # set first time
        tr = self.memory.create_name_write_transaction()
        tr.set_system_identifier(node, "test_idtf")
        result = tr.run()

        self.assertIsNotNone(result)

        # replace
        tr = self.memory.create_name_write_transaction()
        tr.set_system_identifier(node, "test_idtf_replacement")
        result = tr.run()

        self.assertIsNotNone(result)

    def test_replace_system_identifer_check(self):
        tr = self.memory.create_write_transaction()
        node = tr.create_node("node")
        result = tr.run()

        self.assertEqual(len(result), 1)

        node = result[node]

        # set first time
        tr = self.memory.create_name_write_transaction()
        tr.set_system_identifier(node, "test_idtf")
        result = tr.run()

        self.assertIsNotNone(result)

        tr_read = self.memory.create_name_read_transaction()
        node_idtf = tr_read.resolve_by_system_identifier("test_idtf")
        result = tr_read.run()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[node_idtf], node)

        # replace
        tr = self.memory.create_name_write_transaction()
        tr.set_system_identifier(node, "test_idtf_replacement")
        result = tr.run()

        self.assertIsNotNone(result)

        tr_read = self.memory.create_name_read_transaction()
        node_idtf = tr_read.resolve_by_system_identifier(
            "test_idtf_replacement")
        result = tr_read.run()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[node_idtf], node)

    def test_sys_idtf_large(self):

        test_num = 30

        nodes = {}
        tr = self.memory.create_write_transaction()
        for i in range(test_num):
            node = tr.create_node(f"node_{i}")

        result = tr.run()

        self.assertEqual(len(result), test_num)

        for i in range(test_num):
            alias = f"node_{i}"
            el = result[alias]

            nodes[alias] = el
            self.assertIsNotNone(el)

        tr = self.memory.create_name_write_transaction()
        for idtf, el in nodes.items():
            tr.set_system_identifier(el, idtf)

        result = tr.run()
        self.assertIsNotNone(result)

        tr = self.memory.create_name_read_transaction()
        for idtf in nodes.keys():
            tr.resolve_by_system_identifier(idtf)

        result = tr.run()
        self.assertEqual(len(result), test_num)
        for idtf, el in nodes.items():
            self.assertEqual(result[idtf], el)
