from tests.flask_app_case import FlaskAppCase

USERNAME = "test"
PASSWORD = "1234"


class TestRegistation(FlaskAppCase):
    def test_correct_registration(self):
        response = self.client.post(
            "/register",
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("access_token", json_data)

    def test_without_username_registration(self):
        response = self.client.post(
            "/register",
            json={"password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual(
            "Username and/or password is not provided", json_data["message"]
        )

    def test_without_password_registration(self):
        response = self.client.post(
            "/register",
            json={"username": USERNAME},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual(
            "Username and/or password is not provided", json_data["message"]
        )

    def test_for_existing_username_registration(self):
        self.client.post(
            "/register",
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        response = self.client.post(
            "/register",
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual(
            "A user with that username already exists", json_data["message"]
        )


class TestLogin(FlaskAppCase):
    def setUp(self):
        super().setUp()
        self.client.post(
            "/register",
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

    def test_correct_login(self):
        response = self.client.post(
            "/login",
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("access_token", json_data)

    def test_bad_password_login(self):
        response = self.client.post(
            "/login",
            json={"username": USERNAME, "password": f"{PASSWORD}-bad"},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual("Bad username or password", json_data["message"])

    def test_without_username_login(self):
        response = self.client.post(
            "/register",
            json={"password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual(
            "Username and/or password is not provided", json_data["message"]
        )

    def test_without_password_login(self):
        response = self.client.post(
            "/register",
            json={"username": USERNAME},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual(
            "Username and/or password is not provided", json_data["message"]
        )
