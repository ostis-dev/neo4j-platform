from sc.core.transaction.names import TransactionNamesWrite, TransactionNamesRead
from sc.core.client import Client
from sc.core.config import Config
from sc.core.transaction import TransactionWrite, TransactionRead


class Memory:

    def __init__(self, config_path: str):
        self.config = Config(config_path)
        self.client = Client(
            self.config.db_uri(),
            self.config.db_user(),
            self.config.db_password())

    def close(self):
        self.client.close()

    def create_write_transaction(self) -> TransactionWrite:
        return TransactionWrite(self.client.driver)

    def create_read_transaction(self) -> TransactionRead:
        return TransactionRead(self.client.driver)

    def create_name_write_transaction(self) -> TransactionNamesWrite:
        return TransactionNamesWrite(self.client.driver)

    def create_name_read_transaction(self) -> TransactionNamesRead:
        return TransactionNamesRead(self.client.driver)
