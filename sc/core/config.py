import configparser

class Config:

  def __init__(self, config_file):
    self.config = configparser.ConfigParser()
    self.config.read(config_file)

  def _get_value(self, group, name):
    return self.config[group][name]

  def db_name(self):
    return self._get_value("db", "name")

  def db_uri(self):
    return self._get_value("db", "uri")
    
  def db_user(self):
    return self._get_value("db", "user")

  def db_password(self):
    return self._get_value("db", "password")