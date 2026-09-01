from flask import Flask, jsonify

from .routers.health import health_bp
from .routers.todo import todo_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    app.register_blueprint(todo_bp)
    app.register_blueprint(health_bp)

    @app.get("/")
    def index():
        return jsonify({"status": "ok", "message": "Jolt backend is running."})

    return app
