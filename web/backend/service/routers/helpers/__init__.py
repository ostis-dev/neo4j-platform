from functools import wraps

from flask import request
from werkzeug.exceptions import UnsupportedMediaType


def accepts_json_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            raise UnsupportedMediaType("Request data is not JSON")
        return function(*args, **kwargs)

    return wrapper


__all__ = ("accepts_json_only",)
