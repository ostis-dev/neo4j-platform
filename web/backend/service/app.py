import logging

import sc

import tornado.ioloop
import tornado.web

from .config import Config


class App:
    def __init__(self, args) -> None:
        self._args = args
        self._config = Config(args.config)

        self._memory = sc.Memory(self._config.get_path_to_sc_config())

    def run(self):
        application = tornado.web.Application([

        ], cookie_secret=self._config.get_cookie_secret())

        try:
            application.listen(8888)
            tornado.ioloop.IOLoop.instance().start()
            self._on_stop()
        except KeyboardInterrupt:
            print("Interrupted with keyboard...")
            self._on_stop()

    def _on_stop(self):
        print("Stopping service...")
        self._memory.close()
        tornado.ioloop.IOLoop.instance().stop()
