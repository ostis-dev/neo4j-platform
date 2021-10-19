import tornado.web

from .config import Config


class App:
    def __init__(self, args) -> None:
        self._args = args
        self._config = Config(args.config)

    def run(self):
        application = tornado.web.Application([

        ], cookie_secret=self._config.get_cookie_secret())
