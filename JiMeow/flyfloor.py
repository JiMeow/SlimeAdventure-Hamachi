import pygame
from setting import *


class FlyingFloor():

    def __init__(self, win, img, x, y):
        self.win = win
        self.img = pygame.transform.scale(
            pygame.image.load(img), (45, 15))
        self.rect = pygame.Rect(x, y, 45, 15)
        self.height = 15
        self.weight = 45
        self.x = x
        self.y = y

    def draw(self, stage):
        self.win.blit(self.img, (self.x-width*stage, self.y))
