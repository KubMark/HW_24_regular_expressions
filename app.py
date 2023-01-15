from flask import Flask

from views import query_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(query_blueprint)
    return app
