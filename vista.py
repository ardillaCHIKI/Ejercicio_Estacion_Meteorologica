import pygame

class Vista:
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Estaciones Meteorológicas")
        self.fuente = pygame.font.SysFont(None, 24)
        self.reloj = pygame.time.Clock()

    def dibujar(self, estaciones):
        self.pantalla.fill((255, 255, 255))
        x, y = 50, 50
        actual = estaciones.cabeza

        while actual:
            pygame.draw.rect(self.pantalla, (255, 100, 100), (x, y, 40, 40))
            texto = self.fuente.render(actual.dato, True, (0, 0, 0))
            self.pantalla.blit(texto, (x + 50, y + 10))

            sub_actual = actual.sublista.cabeza
            sub_x = x + 120
            while sub_actual:
                pygame.draw.rect(self.pantalla, (100, 200, 255), (sub_x, y, 40, 40))
                sub_txt = self.fuente.render(sub_actual.dato, True, (0, 0, 0))
                self.pantalla.blit(sub_txt, (sub_x + 5, y + 10))
                sub_actual = sub_actual.siguiente
                sub_x += 70

            y += 70
            actual = actual.siguiente

        pygame.display.flip()
        self.reloj.tick(30)

    def salir(self):
        pygame.quit()