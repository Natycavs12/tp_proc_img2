from flask import Flask
from flask_cors import CORS
from routes.image_routes import image_bp
from routes.main_routes import main_bp
import os

app = Flask(__name__)
CORS(app)

app.register_blueprint(main_bp)
app.register_blueprint(image_bp)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))