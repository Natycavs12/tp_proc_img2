import cv2
import numpy as np
from io import BytesIO
from rembg import remove
from PIL import Image, ImageFilter

def to_grayscale(file):
    img = read_image(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return save_image(gray)

def detect_edges(file, params):
    img = read_image(file)
    # aseguramos dict válido
    if not isinstance(params, dict):
        params = {}

    # Obtener los valores de umbral del parámetro
    threshold1 = int(params.get("threshold1", 100)) if params else 100
    threshold2 = int(params.get("threshold2", 200)) if params else 200
    print("CANNY:", threshold1, threshold2, type(threshold1), type(threshold2))

    edges = cv2.Canny(img, threshold1, threshold2)
    return save_image(edges)

def remove_background(file):
    # img = read_image(file)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # _, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
    # wobg = cv2.bitwise_and(img, img, mask=mask)
    # return save_image(wobg)
    #-------------------------
    input_img = read_image(file)
    output_img = remove(input_img)
    return save_image(output_img)

def sepia(file, params):
    img = read_image(file)
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                              [0.349, 0.686, 0.168],
                              [0.272, 0.534, 0.131]])
    intensity = int(params) if params else 100
    sepia_img = cv2.transform(img, sepia_filter)
    # sepia_img = np.clip(sepia_img, 0, params).astype(np.uint8)
    sepia_img = np.clip(sepia_img, 0, 255)
    alpha = intensity / 100.0
    result = cv2.addWeighted(
        sepia_img.astype(np.uint8),
        alpha,
        img,
        1 - alpha,
        0
    )
    return save_image(result)

def calidad(file):
    img = read_image(file)
    # Aumentar la calidad de la imagen (ejemplo: aumentar el contraste)
    alpha = 1.5  # Contraste
    beta = 0     # Brillo
    enhanced_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return save_image(enhanced_img)

def blur(file, params):
    # print(f"Received params in blur function: {params}")
    img = read_image(file)
    # Obtener el valor de desenfoque del parámetro
    blur_value = int(params) if params else 5  # Valor por defecto si no se proporciona
      # asegurar impar
    if blur_value % 2 == 0:
        blur_value += 1
    blurred_img = cv2.GaussianBlur(img, (blur_value, blur_value), 0)
    # blurred_img = img.filter(ImageFilter.GaussianBlur(radius=blur_value))
    return save_image(blurred_img)

def read_image(file):
    file_bytes = np.frombuffer(file.read(), np.uint8)
    return cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

def save_image(img):
    _, buffer = cv2.imencode('.png', img)
    return BytesIO(buffer)