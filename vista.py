import pygame

class WeatherView:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Estaciones Meteorológicas")
        self.font = pygame.font.SysFont(None, 24)
        self.clock = pygame.time.Clock()

    def draw(self, station_list):
        self.screen.fill((255, 255, 255))
        x, y = 50, 50
        station = station_list.head

        while station:
            pygame.draw.rect(self.screen, (255, 100, 100), (x, y, 40, 40))
            text = self.font.render(station.name, True, (0, 0, 0))
            self.screen.blit(text, (x + 50, y + 10))

            weather_node = station.sublist_head
            wx = x + 120
            while weather_node:
                pygame.draw.rect(self.screen, (100, 200, 255), (wx, y, 40, 40))
                wtext = self.font.render(weather_node.data, True, (0, 0, 0))
                self.screen.blit(wtext, (wx + 5, y + 10))
                wx += 70
                weather_node = weather_node.next

            y += 70
            station = station.next

        pygame.display.flip()
        self.clock.tick(30)

    def quit(self):
        pygame.quit()