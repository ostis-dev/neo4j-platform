import os
from typing import Optional

from flask import Flask, current_app


def create_app(test_config: Optional[dict] = None) -> Flask:
    app = Flask(__name__, static_folder="staticfiles")

    from flask_cors import CORS

    CORS(app)

    # General config
    app.config.from_mapping(
        PROPAGATE_EXCEPTIONS=True,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if not test_config:
        from .config import config

        app.secret_key = config.get_secret()
        app.config["API_RESPONSE_MESSAGE_KEY"] = config.get_api_response_message_key()
        app.config["SQLALCHEMY_DATABASE_URI"] = config.get_db_address()
        app.config["JWT_SECRET_KEY"] = app.secret_key
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = config.get_jwt_token_expiration_time()
        app.config["JWT_ERROR_MESSAGE_KEY"] = app.config["API_RESPONSE_MESSAGE_KEY"]
    else:
        app.config.update(test_config)

    from .db import db

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    from flask_jwt_extended import JWTManager

    from .security import user_identity_lookup, user_lookup_callback

    jwt = JWTManager(app)
    jwt.user_identity_loader(user_identity_lookup)
    jwt.user_lookup_loader(user_lookup_callback)

    from flask import json, redirect
    from werkzeug.exceptions import HTTPException

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        response = e.get_response()
        response.data = json.dumps(
            {current_app.config["API_RESPONSE_MESSAGE_KEY"]: e.description}
        )
        response.content_type = "application/json"
        return response

    from .routers import swagger, user

    app.register_blueprint(user.router, url_prefix="/users")
    app.register_blueprint(swagger.router)

    @app.route("/")
    def hello_world():
        return redirect("/docs")

    return app
