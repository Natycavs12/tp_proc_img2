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

        if action == "grayscale":
            result = to_grayscale(file)
        elif action == "edges":
            # threshold = params.get("threshold", 100)
            result = detect_edges(file, params)
        elif action == "remove_bg":
            result = remove_background(file)
        elif action == "sepia":
            intensity = params.get("intensity", 50)
            result = sepia(file, intensity)
        elif action == "calidad":
            result = calidad(file)
        elif action == "blur":
            blur_value = params.get("blur", 5)
            result = blur(file, blur_value )
        elif action == "all":
            result = remove_background(detect_edges(to_grayscale(file)))
        else:
            return {"error": "Acción inválida"}, 400

        return send_file(result, mimetype='image/png')

