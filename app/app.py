import os
import socket
from datetime import datetime, timezone

import psycopg
from flask import Flask, jsonify


app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "production-cloud-platform")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "platformdb")
DB_USER = os.getenv("POSTGRES_USER", "platformuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "platformpass")


def get_db_connection():
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname(),
        "status": "running",
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


@app.route("/ready")
def ready():
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()

        return jsonify({
            "status": "ready",
            "database": "connected",
        }), 200

    except Exception as error:
        return jsonify({
            "status": "not_ready",
            "database": "unavailable",
            "error": str(error),
        }), 503


@app.route("/db-test")
def db_test():
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version()")
                result = cursor.fetchone()

        return jsonify({
            "database": "connected",
            "version": result[0],
        }), 200

    except Exception as error:
        return jsonify({
            "database": "connection_failed",
            "error": str(error),
        }), 500


@app.route("/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname(),
        "database_host": DB_HOST,
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
    )
