from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, current_user, jwt_required
from werkzeug.exceptions import BadRequest, UnprocessableEntity
from werkzeug.security import generate_password_hash

from .helpers import accepts_json_only
from ..models.user import User
from ..security import authenticate

router = Blueprint("auth", __name__)


@router.route("/register", methods=["POST"])
@accepts_json_only
def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    full_name = request.json.get("full_name", None)

    if not (username and password):
        raise BadRequest("Username and/or password is not provided")

    if User.find_by_username(username):
        raise UnprocessableEntity("A user with that username already exists")

    user = User(
        username=username,
        hashed_password=generate_password_hash(password),
        full_name=full_name,
    )
    user.save_to_db()

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token), 201


@router.route("/login", methods=["POST"])
@accepts_json_only
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not (username and password):
        raise BadRequest("Username and/or password is not provided")

    user = authenticate(username, password)
    if user:
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token), 200
    raise BadRequest("Bad username or password")


@router.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    return jsonify(current_user.as_dict())
