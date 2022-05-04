import pygame
from settings import *
from circle import Circle


class CircleGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        for i in range(720):
            Circle(self, small_cir_rad, i/2, "yellow")
            Circle(self, big_cir_rad, i/2, "red")
