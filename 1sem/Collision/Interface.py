import pygame
from src import *


class Interface:
    def __init__(self, display):
        self.Ox = pygame.Rect(10, HEIGHT-20, WIDTH-15, 5)
        self.Oy = pygame.Rect(10, 20, 5, HEIGHT-40)
        self.display = display
        self.count = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw_os(self):
        pygame.draw.rect(self.display, (255, 255, 255), self.Ox)
        pygame.draw.rect(self.display, (255, 255, 255), self.Oy)

    def draw_score(self):
        score = self.font.render(f'Стукнувся:{self.count}', True, (255, 255, 255))
        self.display.blit(score, (WIDTH - 400, 20))
