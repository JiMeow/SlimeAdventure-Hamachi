import pygame
from setting import *


class Collision():
    def __init__(self, p, allp, map):
        self.player = p
        self.allp = allp
        self.map = map

    def setAllPlayer(self, allp):
        self.allp = allp

    def setPlayerX(self, x):
        self.player.x = x

    def setPlayerY(self, y):
        self.player.y = y

    def setPlayerXY(self, x, y):
        self.setPlayerX(x)
        self.setPlayerY(y)

    def setMap(self, map):
        self.map = map

    def setPlayer(self, player):
        self.player = player

    def playerCollideFloor(self):
        if self.player.y >= floor:
            return True, (self.player.x, floor)
        return False, None

    def playerCollideFlyingFloor(self):
        for i in self.map.flyfloor:
            # print(self.player.rect, i.rect)
            if pygame.Rect(self.player.x, self.player.y+self.player.height-1, self.player.width, 1).colliderect(i.rect):
                return True, (self.player.x, i.y-self.player.height+1)
        return False, None

    def playerCollideSpike(self):
        for i in self.map.spike:
            if self.player.rect.colliderect(i.rect):
                return True, (30, -100)
        return False, None
