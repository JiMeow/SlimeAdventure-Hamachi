import pygame
from setting import *


class Map():
    def __init__(self, win, img) -> None:
        self.win = win
        self.img = pygame.transform.scale(
            pygame.image.load(img), (width, height))
        self.gravity = 0.15

    def draw(self):
        self.win.blit(self.img, (0, 0))
