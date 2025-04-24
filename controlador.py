import pygame
from Modelo.tda_lista_lista import Lista, insertar, buscar
from vista import Vista

class Controlador:
    def __init__(self):
        self.estaciones = Lista()
        self.vista = Vista()
        self.ejecutando = True

    def agregar_datos(self):
        estaciones = ['A', 'G', 'L', 'I', 'O', 'Y']
        climas = [
            ['☀', '🌧', '🌫'],
            ['☁', '☀'],
            ['❄', '🌧'],
            ['☀', '☁', '🌧'],
            ['🌧'],
            ['🌫', '🌧']
        ]

        for nombre, estados in zip(estaciones, climas):
            insertar(self.estaciones, nombre)
            nodo = buscar(self.estaciones, nombre)
            for clima in estados:
                insertar(nodo.sublista, clima)

    def correr(self):
        self.agregar_datos()

        while self.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False

            self.vista.dibujar(self.estaciones)

        self.vista.salir()