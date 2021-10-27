from flask import Blueprint
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from ..models.user import User
from ..security import authenticate

router = Blueprint("auth", __name__)


@router.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not (username and password):
        return jsonify({"message": "Username and/or password is not provided"}), 401

    if User.find_by_username(username):
        return {"message": "A user with that username already exists"}, 400

    user = User(
        username=username,
        hashed_password=generate_password_hash(password),
    )
    user.save_to_db()

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token), 201


@router.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not (username and password):
        return jsonify({"message": "Username and/or password is not provided"}), 401

    user = authenticate(username, password)
    if user:
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Bad username or password"}), 401
