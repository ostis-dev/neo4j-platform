import configparser
import os

from typing import KeysView


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

    def get_cookie_secret(self) -> str:
        return self._get_safe_value("tornado", "cookie_secret", "")

    def get_path_to_sc_config(self) -> str:
        path = self._get_safe_value("sc", "config", "")
        if os.path.isabs(path):
            return path

        return os.path.normpath(os.path.join(os.path.dirname(self._path), path))
