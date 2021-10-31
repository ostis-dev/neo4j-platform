from typing import Optional

from flask import Flask, current_app, json, redirect


class App:
    _config = None

    def __init__(self, test_config: Optional[dict] = None):
        self._app = Flask(__name__, static_folder="staticfiles")
        self._configure_app(test_config)
        self._setup_database()
        self._setup_cors()
        self._setup_jwt()
        self._setup_error_handling()
        self._setup_routes()

    @property
    def test_client(self):
        return self._app.test_client

    def _configure_app(self, test_config: Optional[dict] = None):
        # General config
        self._app.config.from_mapping(
            PROPAGATE_EXCEPTIONS=True,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )

        if not test_config:
            from .config import config

            self._app.secret_key = config.get_secret()
            self._app.config["API_RESPONSE_MESSAGE_KEY"] = config.get_api_response_message_key()
            self._app.config["SQLALCHEMY_DATABASE_URI"] = config.get_db_address()
            self._app.config["JWT_SECRET_KEY"] = self._app.secret_key
            self._app.config["JWT_ACCESS_TOKEN_EXPIRES"] = config.get_jwt_token_expiration_time()
            self._app.config["JWT_ERROR_MESSAGE_KEY"] = self._app.config["API_RESPONSE_MESSAGE_KEY"]

            self._config = config
        else:
            self._app.config.update(test_config)

    def _setup_database(self):
        from .db import db

        db.init_app(self._app)

        @self._app.before_first_request
        def create_tables():
            db.create_all()

    def _setup_cors(self):
        from flask_cors import CORS

        CORS(self._app)

    def _setup_jwt(self):
        from flask_jwt_extended import JWTManager

        from .security import user_identity_lookup, user_lookup_callback

        jwt = JWTManager(self._app)
        jwt.user_identity_loader(user_identity_lookup)
        jwt.user_lookup_loader(user_lookup_callback)

    def _setup_error_handling(self):
        from werkzeug.exceptions import HTTPException

        @self._app.errorhandler(HTTPException)
        def handle_exception(e):
            """Return JSON instead of HTML for HTTP errors."""
            response = e.get_response()
            response.data = json.dumps(
                {current_app.config["API_RESPONSE_MESSAGE_KEY"]: e.description}
            )
            response.content_type = "application/json"
            return response

    def _setup_routes(self):
        from .routers import swagger, user

        self._app.register_blueprint(user.router, url_prefix="/users")
        self._app.register_blueprint(swagger.router)

        @self._app.route("/")
        def hello_world():
            return redirect("/docs")

    def run(self, host: Optional[str] = None, port: Optional[int] = None):
        if host and port:
            self._app.run(host, port)
        self._app.run(
            host=self._config.get_host(),
            port=self._config.get_port(),
        )
