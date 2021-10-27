import os
from typing import Optional

from flask import Flask, jsonify


def create_app(test_config: Optional[dict] = None) -> Flask:
    app = Flask(__name__)

    from flask_cors import CORS

    CORS(app)

    from datetime import timedelta

    app.config.from_mapping(
        SECRET_KEY="dev",
        PROPAGATE_EXCEPTIONS=True,
        # SQLAlchemy Setup
        SQLALCHEMY_DATABASE_URI=os.path.join(app.instance_path, "db.sqlite"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # JWT Setup
        JWT_SECRET_KEY="dev",
        JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=7),
        JWT_ERROR_MESSAGE_KEY="message",
    )

    if not test_config:
        from .config import config

        app.secret_key = config.get_secret()
        app.config["SQLALCHEMY_DATABASE_URI"] = config.get_db_address()
        app.config["JWT_SECRET_KEY"] = app.secret_key
    else:
        app.config.update(test_config)

    from .db import db

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    from flask_jwt_extended import JWTManager, current_user, jwt_required

    from .security import user_identity_lookup, user_lookup_callback

    jwt = JWTManager(app)
    jwt.user_identity_loader(user_identity_lookup)
    jwt.user_lookup_loader(user_lookup_callback)

    from .routers import auth

    app.register_blueprint(auth.router)

    @app.route("/")
    def hello_world():
        return jsonify({"message": "Hello World!"})

    # from .sc_memory.helpers.user import create_user_in_memory, check_user_in_memory

    @app.route("/memory_test")
    def test_memory():
        # create_user_in_memory(1)
        # check_user_in_memory(1)

        return jsonify({"message": "ok"})

    @app.route("/jwt_test")
    @jwt_required()
    def jwt_test():
        return jsonify({"username": current_user.username})

    return app
