import sys

import pygame
from src import *
from Cube import Cube
from Interface import Interface
import time


def simulation(mass1, mass2):
    pygame.init()
    pygame.font.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("6 ballov nada")
    clock = pygame.time.Clock()
    interface = Interface(display)
    Cube1 = Cube(x=500, size=50, speed=0, mass=mass1)
    Cube2 = Cube(x=700, size=100, speed=-10, mass=mass2)
    count_frame = 0
    while not (Cube2.speed > 0 and Cube2.speed >= Cube1.speed >= 0) or count_frame <= 500:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        display.fill((0, 0, 0))
        interface.draw_os()
        interface.draw_score()
        if Cube1.check_wall_collision():
            interface.count += 1
        if Cube1.collision_with_cube(Cube2):
            Cube1.speed, Cube2.speed = Cube1.get_speed_after_collision(
                Cube2), Cube2.get_speed_after_collision(Cube1)
            interface.count += 1
        Cube1.move()
        Cube2.move()
        Cube1.draw_cube(display)
        Cube2.draw_cube(display)
        pygame.display.flip()
        if Cube2.speed > 0 and Cube2.speed > Cube1.speed >= 0:
            count_frame += 1
