import cv2
import numpy as np

def apply_morphology(image, operation, kernel_size=5):
    """Aplica operações morfológicas à imagem."""
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    if operation == 'dilation':
        return cv2.dilate(image, kernel, iterations=1)
    elif operation == 'erosion':
        return cv2.erode(image, kernel, iterations=1)
    else:
        raise ValueError("Operação morfológica inválida. Use 'dilation' ou 'erosion'.")