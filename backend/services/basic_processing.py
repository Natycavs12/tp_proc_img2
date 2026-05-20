import cv2
import numpy as np
from io import BytesIO
from rembg import remove
from PIL import Image

def to_grayscale(file):
    img = read_image(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return save_image(gray)

def detect_edges(file):
    img = read_image(file)
    edges = cv2.Canny(img, 100, 200)
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

def sepia(file):
    img = read_image(file)
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                              [0.349, 0.686, 0.168],
                              [0.272, 0.534, 0.131]])
    sepia_img = cv2.transform(img, sepia_filter)
    sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)
    return save_image(sepia_img)

def calidad(file):
    img = read_image(file)
    # Aumentar la calidad de la imagen (ejemplo: aumentar el contraste)
    alpha = 1.5  # Contraste
    beta = 0     # Brillo
    enhanced_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return save_image(enhanced_img)

def read_image(file):
    file_bytes = np.frombuffer(file.read(), np.uint8)
    return cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

def save_image(img):
    _, buffer = cv2.imencode('.png', img)
    return BytesIO(buffer)