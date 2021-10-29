import os
import tempfile
import unittest

from service.app import create_app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()

        app = create_app(
            {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///" + self.db_path}
        )
        self.client = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)
