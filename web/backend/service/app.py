from flask import Flask
from flask import jsonify

from .config import config


def create_app() -> Flask:
    app = Flask(__name__)

    from flask_cors import CORS
    CORS(app)

    from datetime import timedelta

    app.secret_key = config.get_secret()
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # SQLAlchemy Setup
    app.config["SQLALCHEMY_DATABASE_URI"] = config.get_db_address()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # JWT Setup
    app.config["JWT_SECRET_KEY"] = app.secret_key
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
    app.config["JWT_ERROR_MESSAGE_KEY"] = "message"

    from .db import db

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    from flask_jwt_extended import (
        JWTManager,
        jwt_required,
        current_user,
    )
    from .security import user_lookup_callback, user_identity_lookup

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
