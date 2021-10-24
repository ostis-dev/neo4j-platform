from datetime import timedelta

from flask import Flask, jsonify
from flask_jwt import JWT, jwt_required
from flask_restful import Api

from ..config import Config
from .db import db
from .resources.user import UserRegister
from .security import authenticate, identity


def init_app_from_config(config: Config) -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["JWT_SECRET_KEY"] = app.secret_key = config.get_secret()
    app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=60 * 24 * 7)
    app.config["JWT_AUTH_HEADER_PREFIX"] = "Bearer"

    api = Api(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    jwt = JWT(app, authenticate, identity)  # /auth

    api.add_resource(UserRegister, "/register")

    @app.route("/")
    def hello_world():
        return jsonify({"message": "Hello World!"})

    @app.route("/jwt_test")
    @jwt_required()
    def jwt_test():
        return jsonify({"message": "jwt is ok"})

    return app
