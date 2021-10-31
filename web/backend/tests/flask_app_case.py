import os
import tempfile
import unittest
from datetime import timedelta

from service.app import create_app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()

        app = create_app(
            {
                "TESTING": True,
                "SQLALCHEMY_DATABASE_URI": f"sqlite:///{self.db_path}",
                "JWT_SECRET_KEY": "dev",
                "JWT_ACCESS_TOKEN_EXPIRES": timedelta(days=7),
                "JWT_ERROR_MESSAGE_KEY": "message",
                "API_RESPONSE_MESSAGE_KEY": "message",
            }
        )
        self.client = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)
