# backend/routes/image_routes.py
from flask import Blueprint, request, send_file
# from services.basic_processing import to_grayscale, detect_edges, remove_background, sepia, calidad, blur
from services.basic_processing import ImageProcessor
from flask import jsonify
import json

image_bp = Blueprint("image_bp", __name__)
processor = ImageProcessor() #Instanciar la clase ImageProcessor

@image_bp.route("/process", methods=["GET","POST"])
def process_image():
    if request.method == "GET":
        return jsonify({"message": "Endpoint de procesamiento de imágenes. Use POST para enviar una imagen y una acción."})
    elif request.method == "POST":

        file = request.files.get("image")
        print("Archivo recibido:", file.filename if file else None)
        raw = file.read()
        print("Bytes recibidos:", len(raw))
        file.seek(0)  # importante: volver al inicio después de leer para el chequeo
        file = request.files["image"]
        action = request.form.get("action")
        params = json.loads(request.form.get("params")) if request.form.get("params") else {}

        print(f"\n\nReceived action: {action}, params: {params}\n\n")
        if not file or not action:
            return {"error": "missing data"}, 400

        actions = {
            "grayscale": processor.to_grayscale(file),
            "edges": processor.detect_edges(file, params),
            "remove_bg": processor.remove_background(file),
            "sepia": processor.sepia(file, params.get("intensity", 50)),
            "calidad": processor.calidad(file),
            "blur": processor.blur(file, params.get("blur", 5)),
            "all": processor.remove_background(processor.detect_edges(processor.to_grayscale(file), params))
        }

        if action in actions:
            result = actions[action]
        else:
            return {"error": "Acción inválida"}, 400

        return send_file(result, mimetype='image/png')
