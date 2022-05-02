import pygame
from setting import *
from flyfloor import FlyingFloor


class Map():
    def __init__(self, win, img) -> None:
        self.win = win
        self.img = pygame.transform.scale(
            pygame.image.load(img), (width, height))
        self.gravity = 0.3
        self.flyfloor = []
        for i in range(10):
            self.addflyfloor(500+45*i, 540)

    def addflyfloor(self, x, y):
        self.flyfloor.append(FlyingFloor(
            self.win, "JiMeow/photo/flyfloor.png", x, y))

    def draw(self):
        self.win.blit(self.img, (0, 0))
        for i in self.flyfloor:
            i.draw()
