from typing import TYPE_CHECKING

from flask import Flask

if TYPE_CHECKING:
    from ..config import Config
    from sc import Memory


def create_app(config: "Config", memory: "Memory") -> Flask:
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

    from sc.core.transaction import TransactionWrite, TransactionNamesRead
    from sc.core.types import (
        NodeType,
        ArcType,
        LinkType,
        TypeArcPos,
        TypeConst,
        TypeArcPerm,
    )

    NodeConst = NodeType(const=TypeConst.CONST)
    LinkConst = LinkType(const=TypeConst.CONST)
    ArcMemberConstPosPerm = ArcType(
        const=TypeConst.CONST,
        arc_pos=TypeArcPos.POS,
        arc_perm=TypeArcPerm.PERM,
        is_member=True,
    )
    ArcNoMemberConstPosPerm = ArcType(
        const=TypeConst.CONST,
        arc_pos=TypeArcPos.POS,
        arc_perm=TypeArcPerm.PERM,
        is_member=False,
    )

    @app.route("/memory_test")
    def test_memory():
        tr = TransactionNamesRead(memory.driver)
        user = tr.resolve_by_system_identifier("user")
        result = tr.run()

        try:
            user = result[user]
        except KeyError:
            tr = TransactionWrite(memory.driver)
            user = tr.create_node(NodeConst, alias="user")
            result = tr.run()
            user = result[user]

        tr = TransactionWrite(memory.driver)
        user_instance = tr.create_node(NodeConst, alias="user_instance")
        _ = tr.create_edge(user, user_instance, ArcMemberConstPosPerm)
        link = tr.create_link_with_content(LinkConst, content=f"{1}", is_url=False)
        edge = tr.create_edge(user_instance, link, ArcNoMemberConstPosPerm)
        nrel_user_id = tr.create_node(NodeConst, alias="nrel_user_id")
        _ = tr.create_edge(nrel_user_id, edge, ArcMemberConstPosPerm)
        result = tr.run()
        print(result[user_instance])

        return jsonify({})

    @app.route("/jwt_test")
    @jwt_required()
    def jwt_test():
        return jsonify({"username": current_identity.username})

    return app
