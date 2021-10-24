import logging

import sc

from .config import Config


class App:
    def __init__(self, args) -> None:
        self._args = args
        self._config = Config(args.config)

        self._memory = sc.Memory(self._config.get_path_to_sc_config())

    def run(self):
        from flask import Flask

        app = Flask(__name__)

        try:
            app.run(self._config.get_host(), self._config.get_port())
            self._on_stop()
        except KeyboardInterrupt:
            print("Interrupted with keyboard...")
            self._on_stop()

    def _on_stop(self):
        print("Stopping service...")
        self._memory.close()
