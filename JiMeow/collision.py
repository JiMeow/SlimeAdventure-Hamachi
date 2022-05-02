import pygame
from setting import *


class Collision():
    def __init__(self, p, allp, map):
        self.player = p
        self.allp = allp
        self.map = map

    def addAllPlayer(self, allp):
        self.allp = allp

    def addPlayerX(self, x):
        self.player.x = x

    def addPlayerY(self, y):
        self.player.y = y

    def addPlayerXY(self, x, y):
        self.addPlayerX(x)
        self.addPlayerY(y)

    def addMap(self, map):
        self.map = map

    def addPlayer(self, player):
        self.player = player

    def playerCollideFloor(self):
        if self.player.y >= floor:
            return True, (self.player.x, floor)
        return False, None

    def playerCollideFlyingFloor(self):
        for i in self.map.flyfloor:
            if pygame.Rect(self.player.x, self.player.y+self.player.height-1, self.player.width, 1).colliderect(i.rect):
                return True, (self.player.x, i.y-self.player.height+1)
        return False, None
