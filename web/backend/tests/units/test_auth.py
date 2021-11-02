from tests.flask_app_case import FlaskAppTestCase

ROUTES_PREFIX = "/users"
REGISTRATION_ROUTE = "/register"
LOGIN_ROUTE = "/login"
CURRENT_USER_ROUTE = "/me"

USERNAME = "test"
PASSWORD = "1234"


def urljoin(root_url, *urls) -> str:
    return "/".join((root_url, *(url.lstrip("/") for url in urls)))


class TestRegistration(FlaskAppTestCase):
    def test_correct_registration(self):
        response = self.client.post(
            urljoin(ROUTES_PREFIX, REGISTRATION_ROUTE),
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("access_token", json_data)

    def test_without_username_registration(self):
        response = self.client.post(
            urljoin(ROUTES_PREFIX, REGISTRATION_ROUTE),
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
            urljoin(ROUTES_PREFIX, REGISTRATION_ROUTE),
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
            urljoin(ROUTES_PREFIX, REGISTRATION_ROUTE),
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        response = self.client.post(
            urljoin(ROUTES_PREFIX, REGISTRATION_ROUTE),
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual(
            "A user with that username already exists", json_data["message"]
        )


class TestLogin(FlaskAppTestCase):
    def setUp(self):
        super().setUp()
        self.client.post(
            urljoin(ROUTES_PREFIX, REGISTRATION_ROUTE),
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

    def test_correct_login(self):
        response = self.client.post(
            urljoin(ROUTES_PREFIX, LOGIN_ROUTE),
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("access_token", json_data)

    def test_bad_password_login(self):
        response = self.client.post(
            urljoin(ROUTES_PREFIX, LOGIN_ROUTE),
            json={"username": USERNAME, "password": f"{PASSWORD}-bad"},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual("Bad username or password", json_data["message"])

    def test_without_username_login(self):
        response = self.client.post(
            urljoin(ROUTES_PREFIX, LOGIN_ROUTE),
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
            urljoin(ROUTES_PREFIX, LOGIN_ROUTE),
            json={"username": USERNAME},
            follow_redirects=True,
        )

        json_data = response.get_json()

        self.assertIn("message", json_data)
        self.assertEqual(
            "Username and/or password is not provided", json_data["message"]
        )


class TestGetCurrentUser(FlaskAppTestCase):
    def setUp(self):
        super().setUp()
        self.client.post(
            urljoin(ROUTES_PREFIX, REGISTRATION_ROUTE),
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        response = self.client.post(
            urljoin(ROUTES_PREFIX, LOGIN_ROUTE),
            json={"username": USERNAME, "password": PASSWORD},
            follow_redirects=True,
        )

        json_data = response.get_json()
        self.access_token = json_data.get("access_token")

    def test_correct_get_me(self):
        response = self.client.get(
            urljoin(ROUTES_PREFIX, CURRENT_USER_ROUTE),
            headers={"Authorization": f"Bearer {self.access_token}"},
        )

        json_data = response.get_json()

        self.assertIn("username", json_data)
        self.assertEqual(USERNAME, json_data["username"])

    def test_get_me_without_token(self):
        response = self.client.get(
            urljoin(ROUTES_PREFIX, CURRENT_USER_ROUTE),
        )

        json_data = response.get_json()

        self.assertNotIn("username", json_data)
        self.assertIn("message", json_data)
        self.assertEqual("Missing Authorization Header", json_data["message"])
