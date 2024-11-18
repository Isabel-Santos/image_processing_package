# image_processing_package

Pacote para processamento de imagens. 
O pacote `image_processing_package` é usado para:
	- Aplicar filtros a imagens
	- Detectar bordas em imagens
	- Realizar operações morfológicas
	- Manipular e exibir imagens

## Installation

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar `image_processing_package`.

```bash
pip install image_processing_package
```

## Usage

python
from image_processing.utils import read_image, save_image, display_image
from image_processing.processing import apply_filter, detect_edges

# Ler uma imagem
image = read_image('caminho/para/imagem.jpg')

# Detectar bordas
edges = detect_edges(image)

# Exibir a imagem com bordas detectadas
display_image(edges, 'Bordas Detectadas')

# Salvar a imagem com bordas
save_image('caminho/para/salvar/bordas.jpg', edges)


## Author
Isabel Santos

## License
[MIT](https://choosealicense.com/licenses/mit/)