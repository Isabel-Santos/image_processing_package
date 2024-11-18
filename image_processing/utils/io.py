import cv2

def read_image(filepath):
    """Lê uma imagem do disco."""
    return cv2.imread(filepath)

def save_image(filepath, image):
    """Salva uma imagem no disco."""
    cv2.imwrite(filepath, image)