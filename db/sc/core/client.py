from neo4j import GraphDatabase
import neo4j
from neo4j.work.result import Result


class Client:

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    @property
    def driver(self) -> neo4j.Neo4jDriver:
        return self._driver

    def close(self):
        self._driver.close()

    def list_databases(self):
        with self._driver.session() as session:
            return session.read_transaction(Client._list_db)

    def has_db(self, db):
        return db in self.list_databases()

    @neo4j.unit_of_work(timeout=5)
    def _list_db(tx: neo4j.Transaction):
        result = tx.run("SHOW DATABASES")

        db_list = []
        for r in result:
            db_list.append(r[0])

        return db_list
