from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, current_user, jwt_required
from werkzeug.security import generate_password_hash

from ..models.user import User
from ..security import authenticate

router = Blueprint("auth", __name__)


@router.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)
    full_name = data.get("full_name", None)

    if not (username and password):
        return jsonify({"message": "Username and/or password is not provided"}), 400

    if User.find_by_username(username):
        return {"message": "A user with that username already exists"}, 409

    user = User(
        username=username,
        hashed_password=generate_password_hash(password),
        full_name=full_name,
    )
    user.save_to_db()

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token), 201


@router.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    if not (username and password):
        return jsonify({"message": "Username and/or password is not provided"}), 400

    user = authenticate(username, password)
    if user:
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Bad username or password"}), 400


@router.route("/users/me", methods=["GET"])
@jwt_required()
def get_current_user():
    return jsonify(current_user.as_dict())
