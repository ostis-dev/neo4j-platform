from sc.core.keywords import Labels
from sc.core.types import NodeType, TypeConst
from tests.memory_case import MemoryTestCase

from sc.core.transaction import *
from tests.units.core.test_transaction_read import NodeConst

NodeConst = NodeType(const=TypeConst.CONST)


class TestNames(MemoryTestCase):

    def test_set_system_identifer_dummy(self):
        tr = TransactionWrite(self.memory.driver)
        node = tr.create_node(NodeConst, alias="node")
        node2 = tr.create_node(NodeConst, alias="node2")
        result = tr.run()

        self.assertEqual(len(result), 2)

        node = result[node]
        node2 = result[node2]

        tr = TransactionNamesWrite(self.memory.driver)
        tr.set_system_identifier(node, "node_sys_idtf")
        tr.set_system_identifier(node2, "node_sys_idtf2")
        result = tr.run()

        self.assertIsNotNone(result)

    def test_replace_system_identifer_dummy(self):
        tr = TransactionWrite(self.memory.driver)
        node = tr.create_node(NodeConst, alias="node")
        result = tr.run()

        self.assertEqual(len(result), 1)

        node = result[node]

        # set first time
        tr = TransactionNamesWrite(self.memory.driver)
        tr.set_system_identifier(node, "test_idtf")
        result = tr.run()

        self.assertIsNotNone(result)

        # replace
        tr = TransactionNamesWrite(self.memory.driver)
        tr.set_system_identifier(node, "test_idtf_replacement")
        result = tr.run()

        self.assertIsNotNone(result)

    def test_replace_system_identifer_check(self):
        tr = TransactionWrite(self.memory.driver)
        node = tr.create_node(NodeConst, alias="node")
        result = tr.run()

        self.assertEqual(len(result), 1)

        node = result[node]

        # set first time
        tr = TransactionNamesWrite(self.memory.driver)
        tr.set_system_identifier(node, "test_idtf")
        result = tr.run()

        self.assertIsNotNone(result)

        tr_read = TransactionNamesRead(self.memory.driver)
        node_idtf = tr_read.resolve_by_system_identifier("test_idtf")
        result = tr_read.run()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[node_idtf], node)

        # replace
        tr = TransactionNamesWrite(self.memory.driver)
        tr.set_system_identifier(node, "test_idtf_replacement")
        result = tr.run()

        self.assertIsNotNone(result)

        tr_read = TransactionNamesRead(self.memory.driver)
        node_idtf = tr_read.resolve_by_system_identifier(
            "test_idtf_replacement")
        result = tr_read.run()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[node_idtf], node)

    def test_sys_idtf_large(self):

        test_num = 30

        nodes = {}
        tr = TransactionWrite(self.memory.driver)
        for i in range(test_num):
            node = tr.create_node(NodeConst, alias=f"node_{i}")

        result = tr.run()

        self.assertEqual(len(result), test_num)

        for i in range(test_num):
            alias = f"node_{i}"
            el = result[alias]

            nodes[alias] = el
            self.assertIsNotNone(el)

        tr = TransactionNamesWrite(self.memory.driver)
        for idtf, el in nodes.items():
            tr.set_system_identifier(el, idtf)

        result = tr.run()
        self.assertIsNotNone(result)

        tr = TransactionNamesRead(self.memory.driver)
        for idtf in nodes.keys():
            tr.resolve_by_system_identifier(idtf)

        result = tr.run()
        self.assertEqual(len(result), test_num)
        for idtf, el in nodes.items():
            self.assertEqual(result[idtf], el)
