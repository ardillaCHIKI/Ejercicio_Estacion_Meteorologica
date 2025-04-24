from Modelo.modelo import SistemaMeteorologico
from Controlador.controlador import Controlador
from Vista.vista import VistaGradio

# Inicialización
sistema_meteorologico = SistemaMeteorologico()
controlador = Controlador(sistema_meteorologico)
vista = VistaGradio(controlador)

# Lanzar la interfaz
vista.mostrar_interfaz()