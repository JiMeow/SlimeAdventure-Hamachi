import pygame
from setting import *


class Spike():

    def __init__(self, win, x, y, stage):
        self.win = win
        self.img = pygame.transform.scale(
            pygame.image.load("JiMeow/photo/spike1.png"), (70, 50))
        self.width = 70
        self.height = 50
        self.x = x + width * stage
        self.y = y
        self.rect = pygame.Rect(self.x, y, 70, 50)

    def draw(self, stage):
        self.win.blit(self.img, (self.x-width*stage, self.y))
