from .processing.filter import *  # Importa tudo do módulo filter
from .processing.edge_detection import *  # Importa tudo do módulo edge_detection
from .processing.morphology import *  # Importa tudo do módulo morphology
from .utils.io import *  # Importa tudo do módulo io
from .utils.plot import *  # Importa tudo do módulo plot

__all__ = [
    "filter", 
    "edge_detection", 
    "morphology", 
    "io", 
    "plot"
]