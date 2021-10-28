import json
import os
from urllib.parse import urljoin

from flask import Blueprint, current_app, jsonify
from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_UI_ROUTE = "/docs"
SWAGGER_FILE = "openapi.json"
SWAGGER_FILE_ROUTE = f"/{SWAGGER_FILE}"


router = Blueprint("swagger", __name__)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_UI_ROUTE,
    SWAGGER_FILE_ROUTE,
    config={
        "app_name": "OSTIS",
    },
)

router.register_blueprint(swaggerui_blueprint)


@router.route(SWAGGER_FILE_ROUTE)
def get_swagger_specification():
    return current_app.send_static_file(SWAGGER_FILE)
