import matplotlib.pyplot as plt

def display_image(image, title='Imagem'):
    """Exibe uma imagem usando matplotlib."""
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()