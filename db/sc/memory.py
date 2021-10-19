from sc.core.client import Client
from sc.core.config import Config
from sc.core.transaction import TransactionWrite, TransactionRead, TransactionNamesWrite, TransactionNamesRead

import neo4j


class Memory:

    def __init__(self, config_path: str):
        self._config = Config(config_path)

        print(f"Connecting to {self._config.db_uri()}")
        self._client = Client(
            self._config.db_uri(),
            self._config.db_user(),
            self._config.db_password())

    def close(self):
        print(f"Close connection to {self._config.db_uri()}")
        self._client.close()

    @property
    def driver(self) -> neo4j.Neo4jDriver:
        return self._client.driver

    @property
    def client(self) -> Client:
        return self._client

    def create_transaction_read(self) -> TransactionRead:
        return TransactionRead(self.driver)

    def create_transaction_write(self) -> TransactionWrite:
        return TransactionWrite(self.driver)

    def create_transaction_names_read(self) -> TransactionNamesRead:
        return TransactionNamesRead(self.driver)

    def create_transaction_names_write(self) -> TransactionNamesWrite:
        return TransactionNamesWrite(self.driver)
