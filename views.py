import os
from typing import Any

from flask import Blueprint, request, Response, abort

from functions import execute

query_blueprint = Blueprint("perform_query", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@query_blueprint.post('/perform_query')
def perform_query() -> Response:
    # Check request
    data: Any = request.json
    if "queries" not in data.keys() or "file_name" not in data.keys():
        abort(400, description="Check filename or query")

    #Check filename
    filename = os.path.join(DATA_DIR, data['file_name'])
    if not os.path.exists(filename):
        abort(400, "File does not exist")

    queries = data["queries"]
    return execute(queries, filename)



