import os
import pygame
from modelo import StationList
from vista import WeatherView

class WeatherController:
    def __init__(self):
        # Inicializar modelo y vista
        self.model = StationList()
        self.view = WeatherView()
        self.running = True

    def run(self):
        # Deshabilitar el sonido de pygame
        os.environ["SDL_AUDIODRIVER"] = "dummy"

        # Inicializar pygame
        pygame.init()

        # Crear datos de ejemplo
        estaciones = ['A', 'G', 'L', 'I', 'O', 'Y']
        climas = [
            ['☀', '🌧', '🌫'],
            ['☁', '☀'],
            ['❄', '🌧'],
            ['☀', '☁', '🌧'],
            ['🌧'],
            ['🌫', '🌧']
        ]

        # Agregar estaciones y climas al modelo
        for nombre, datos in zip(estaciones, climas):
            estacion = self.model.add_station(nombre)
            for clima in datos:
                estacion.add_weather(clima)

        # Bucle principal
        try:
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                self.view.draw(self.model)
        except Exception as e:
            print(f"Error durante la ejecución: {e}")
        finally:
            # Finalizar pygame y cerrar la vista
            self.view.quit()
            pygame.quit()