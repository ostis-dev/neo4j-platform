from werkzeug.security import check_password_hash
from .models.user import User
from typing import Optional


def authenticate(username, password) -> Optional[User]:
    user = User.find_by_username(username)
    if user and check_password_hash(user.hashed_password, password):
        return user


def user_identity_lookup(user: User) -> str:
    return user.id


def user_lookup_callback(_jwt_header, jwt_data) -> Optional[User]:
    user_id = jwt_data["sub"]
    return User.find_by_id(user_id)
