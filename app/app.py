from flask import Flask, jsonify
import os
import socket
from datetime import datetime, timezone

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "production-cloud-platform")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname(),
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


@app.route("/ready")
def ready():
    return jsonify({
        "status": "ready"
    }), 200


@app.route("/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
