from Modelo.modelo import SistemaMeteorologico
from Controlador.controlador import Controlador
from Vista.vista import VistaGradio

# Inicialización con estaciones meteorológicas predefinidas
sistema_meteorologico = SistemaMeteorologico()
controlador = Controlador(sistema_meteorologico)
vista = VistaGradio(controlador)

# Lanzar la interfaz con diseño mejorado
vista.mostrar_interfaz()