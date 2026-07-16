import cv2
import numpy as np
import pillow_avif  # habilita que Pillow pueda abrir archivos .avif
from io import BytesIO
from rembg import remove
from PIL import Image


#Clase que encapsula la lectura y escritura de imágenes
class ImageIO: 
    def read(self, file):
        file.seek(0)  # por si el archivo ya fue leído antes
        # file_bytes = np.frombuffer(file.read(), np.uint8)
        # return cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Usamos Pillow en vez de cv2.imdecode porque soporta más formatos
        # (como .avif, .webp, etc). cv2.imdecode devuelve None con AVIF
        # sin tirar error, y eso rompe mas adelante.
        pil_img = Image.open(file).convert("RGB")
        img_array = np.array(pil_img)
        # Pillow entrega RGB, OpenCV trabaja en BGR
        return cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    def save(self, img):
        _, buffer = cv2.imencode('.png', img)
        return BytesIO(buffer)


#Clase que agrupa los métodos de procesamiento de imágenes
class ImageProcessor:
    def __init__(self):
        self.io = ImageIO()

    def to_grayscale(self, file):
        img = self.io.read(file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return self.io.save(gray)

    def detect_edges(self, file, params):
        img = self.io.read(file)
        if not isinstance(params, dict):
            params = {}

        threshold1 = int(params.get("threshold1", 100))
        threshold2 = int(params.get("threshold2", 200))

        edges = cv2.Canny(img, threshold1, threshold2)
        return self.io.save(edges)

    def remove_background(self, file):
        img = self.io.read(file)
        output_img = remove(img)
        return self.io.save(output_img)

    def sepia(self, file, params):
        img = self.io.read(file)
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                                  [0.349, 0.686, 0.168],
                                  [0.272, 0.534, 0.131]])

        intensity = int(params) if params else 100
        sepia_img = cv2.transform(img, sepia_filter)
        sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)

        alpha = intensity / 100.0
        result = cv2.addWeighted(sepia_img, alpha, img, 1 - alpha, 0)
        return self.io.save(result)

    def calidad(self, file):
        img = self.io.read(file)
        alpha = 1.5  # contraste
        beta = 0     # brillo
        enhanced_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        return self.io.save(enhanced_img)

    def blur(self, file, params):
        img = self.io.read(file)
        blur_value = int(params) if params else 5

        if blur_value % 2 == 0:
            blur_value += 1

        blurred_img = cv2.GaussianBlur(img, (blur_value, blur_value), 0)
        return self.io.save(blurred_img)
