import cv2

def detect_edges(image):
    """Detecta bordas na imagem usando o método Canny."""
    return cv2.Canny(image, 100, 200)