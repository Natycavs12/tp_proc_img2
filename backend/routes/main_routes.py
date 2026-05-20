# backend/routes/main_routes.py
from flask import Blueprint, request, send_file
from flask import jsonify


main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def main():
    return jsonify({"message": "Endpoint del menú principal."})
