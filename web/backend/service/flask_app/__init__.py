from flask import Flask

from .sc_memory_helpers.user import create_user_in_memory, check_user_in_memory
from .settings import settings as config


def create_app() -> Flask:
    app = Flask(__name__)

    from datetime import timedelta

    app.secret_key = config.get_secret()
    app.config["SQLALCHEMY_DATABASE_URI"] = config.get_db_address()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # JWT Setup
    app.config["JWT_SECRET_KEY"] = app.secret_key
    app.config["JWT_EXPIRATION_DELTA"] = timedelta(days=7)
    app.config["JWT_AUTH_HEADER_PREFIX"] = "Bearer"
    app.config["JWT_AUTH_URL_RULE"] = "/login"

    from .db import db

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    from flask_jwt import JWT, jwt_required, current_identity
    from .security import authenticate, identity

    jwt = JWT(app, authenticate, identity)  # /login

    from flask_restful import Api
    from .resources.user import UserRegister

    api = Api(app)

    api.add_resource(UserRegister, "/register")

    from flask import jsonify

    @app.route("/")
    def hello_world():
        return jsonify({"message": "Hello World!"})

    @app.route("/memory_test")
    def test_memory():
        # create_user_in_memory(1)
        # check_user_in_memory(1)

        return jsonify({"message": "ok"})

    @app.route("/jwt_test")
    @jwt_required()
    def jwt_test():
        return jsonify({"username": current_identity.username})

    return app
