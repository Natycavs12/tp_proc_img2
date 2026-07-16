# backend/routes/image_routes.py
from flask import Blueprint, request, send_file
from services.basic_processing import to_grayscale, detect_edges, remove_background, sepia, calidad, blur
from flask import jsonify
import json


image_bp = Blueprint("image_bp", __name__)

@image_bp.route("/process", methods=["GET","POST"])
def process_image():
    if request.method == "GET":
        return jsonify({"message": "Endpoint de procesamiento de imágenes. Use POST para enviar una imagen y una acción."})
    elif request.method == "POST":

        file = request.files["image"]
        action = request.form.get("action")
        params = json.loads(request.form.get("params")) if request.form.get("params") else {}

        print(f"\n\nReceived action: {action}, params: {params}\n\n")
        if not file or not action:
            return {"error": "missing data"}, 400

        actions = {
            "grayscale": to_grayscale(file),
            "edges": detect_edges(file, params),
            "remove_bg": remove_background(file),
            "sepia": sepia(file, params.get("intensity", 50)),
            "calidad": calidad(file),
            "blur": blur(file, params.get("blur", 5)),
            "all": remove_background(detect_edges(to_grayscale(file)))
        }

        if action in actions:
            result = actions[action]
        else:
            return {"error": "Acción inválida"}, 400

        return send_file(result, mimetype='image/png')
