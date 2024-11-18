import cv2
import numpy as np

def apply_filter(image, kernel):
    """Aplica um filtro à imagem utilizando um kernel."""
    return cv2.filter2D(image, -1, kernel)