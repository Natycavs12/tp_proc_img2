# backend/routes/image_routes.py
from flask import Blueprint, request, send_file
from services.basic_processing import to_grayscale, detect_edges, remove_background, sepia, calidad
from flask import jsonify


image_bp = Blueprint("image_bp", __name__)

@image_bp.route("/process", methods=["GET","POST"])
def process_image():
    if request.method == "GET":
        return jsonify({"message": "Endpoint de procesamiento de imágenes. Use POST para enviar una imagen y una acción."})
    elif request.method == "POST":

        file = request.files["image"]
        action = request.form.get("action")

        if action == "grayscale":
            result = to_grayscale(file)
        elif action == "edges":
            result = detect_edges(file)
        elif action == "remove_bg":
            result = remove_background(file)
        elif action == "sepia":
            result = sepia(file)
        elif action == "calidad":
            result = calidad(file)
        elif action == "all":
            result = remove_background(detect_edges(to_grayscale(file)))
        else:
            return {"error": "Acción inválida"}, 400

        return send_file(result, mimetype='image/png')

