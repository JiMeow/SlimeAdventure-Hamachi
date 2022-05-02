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
        self.stage = list(range(2))

    def addflyfloor(self, x, y):
        self.flyfloor.append(FlyingFloor(
            self.win, "JiMeow/photo/flyfloor.png", x, y))

    def draw(self, stage):
        self.win.blit(self.img, (0, 0))
        if stage in self.stage:
            eval("self.stage"+str(int(stage))+"()")

    def stage0(self):
        self.flyfloor = []
        for i in range(10):
            self.addflyfloor(500+45*i, 540)
        for i in range(10):
            self.addflyfloor(950+45*i, 440)
        for i in self.flyfloor:
            i.draw(0)

    def stage1(self):
        self.flyfloor = []
        for i in range(2):
            self.addflyfloor(width*1+45*i, 440)
        for i in range(20):
            self.addflyfloor(width*1+45*i, 340)
        for i in self.flyfloor:
            i.draw(1)
