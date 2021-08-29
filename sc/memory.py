from sc.client import Client
from sc.config import Config
from sc.transaction import TransactionWrite

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
