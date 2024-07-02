import pygame
from src import *


class Cube:
    def __init__(self, x, size, speed, mass):
        self.x = x - size
        self.y = HEIGHT - size - 20
        self.size = size
        self.speed = speed
        self.mass = mass
        self.color = (255, 255, 255)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def collision_with_cube(self, cube2):
        if self.x + self.size >= cube2.x:
            return True
        else:
            return False

    def move(self):
        self.x += self.speed

    def draw_cube(self, display):
        pygame.draw.rect(display, self.color, self.get_rect())

    def get_speed_after_collision(self, cube2):
        return ((self.mass - cube2.mass) / (self.mass + cube2.mass)) * self.speed + \
               ((2 * cube2.mass) / (self.mass + cube2.mass)) * cube2.speed

    def check_wall_collision(self):
        if self.x <= 15:
            self.x = 15
            self.speed *= -1
            return True
        return False
