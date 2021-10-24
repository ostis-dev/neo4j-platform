import configparser
import os

from typing import KeysView
from secrets import token_hex


class Config:

    def __init__(self, path) -> None:
        self._path = path
        self._config = configparser.ConfigParser()
        self._config.read(path)

    def _get_safe_value(self, section: str, key: str, default: str = "") -> str:
        try:
            return self._config[section][key]
        except KeyError:
            return default

    def get_secret(self) -> str:
        return self._get_safe_value("flask", "secret", token_hex(32))

    def get_host(self) -> str:
        return self._get_safe_value("flask", "host", "127.0.0.1")

    def get_port(self) -> int:
        return int(self._get_safe_value("flask", "port", "5000"))


    def get_path_to_sc_config(self) -> str:
        path = self._get_safe_value("sc", "config", "")
        if os.path.isabs(path):
            return path

        return os.path.normpath(os.path.join(os.path.dirname(self._path), path))
