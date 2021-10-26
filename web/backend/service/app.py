import logging

import sc


class App:
    def __init__(self, args) -> None:
        self._args = args
        # self._config = Config(args.config)

        # self._memory = sc.Memory(self._config.get_path_to_sc_config())

    def run(self):
        from .flask_app import create_app
        from .flask_app.settings import settings as config

        app = create_app()

        try:
            app.run(config.get_host(), config.get_port())
            self._on_stop()
        except KeyboardInterrupt:
            print("Interrupted with keyboard...")
            self._on_stop()

    def _on_stop(self):
        print("Stopping service...")
        # self._memory.close()
