from flask import jsonify
from typing import Any

def ok(message: dict[str, Any] | list[dict[str, Any]], status=200):
    return jsonify(message), status

def err(message: str, status=400):
    payload = {
        "ok": False,
        "status": status,
        "message": message,
    }
    return jsonify(payload), status
