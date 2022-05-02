import pygame
from setting import *


class Layout():
    def __init__(self, win):
        self.win = win
        self.dt = 1/60
        self._eval = []

    def setPlayer(self, player):
        self.player = player

    def setAllPlayer(self, player):
        self.allp = player

    def setScreen(self, screen):
        self.screen = screen

    def setEval(self, command):
        self._eval.append(command)

    def setDt(self, dt):
        self.dt = dt

    def setCollision(self, collision):
        self.collision = collision

    def drawPlayerFrame(self):
        stage = self.player.x//width
        self.screen.draw(stage)
        for i in self._eval:
            eval(i)
        for i in self.allp:
            if i.id != self.player.id:
                i.draw(self.win, stage)
                i.drawname(self.win, stage)
        for i in self.allp:
            if i.id == self.player.id:
                self.collision.setPlayer(i)
                self.player.update(self.dt, self.collision)
                self.player.draw(self.win, stage)
                self.player.drawname(self.win, stage)
        pygame.display.update()
