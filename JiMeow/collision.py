import pygame
from setting import *


class Collision():
    def __init__(self, p, allp, map):
        self.p = p
        self.allp = allp
        self.map = map

    def addAllPlayer(self, allp):
        self.allp = allp

    def addMap(self, map):
        self.map = map

    def addPlayer(self, player):
        self.player = player

    def playerCollideFlyingFloor(self):
        for i in self.map.flyfloor:
            if self.player.rect.colliderect(i.rect):
                return True
        return False

    def playerCollideFloor(self):
        if self.player.y >= floor:
            return True
        return False
