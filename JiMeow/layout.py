import pygame
from setting import *


class Layout():
    def __init__(self, win):
        self.win = win
        self.dt = 1/60
        self._eval = []

    def addPlayer(self, player):
        self.player = player

    def addAllPlayer(self, player):
        self.allp = player

    def addScreen(self, screen):
        self.screen = screen

    def addEval(self, command):
        self._eval.append(command)

    def addDt(self, dt):
        self.dt = dt

    def draw(self):
        self.screen.draw()
        for i in self._eval:
            eval(i)
        for i in self.allp:
            if i.id != self.player.id:
                i.draw(self.win)
                i.drawname(self.win)
        for i in self.allp:
            if i.id == self.player.id:
                self.player.update(self.dt)
                self.player.draw(self.win)
                self.player.drawname(self.win)
        pygame.display.update()

    def drawPlayerFrame(self):
        self.screen.draw()
        stage = self.player.x//width
        for i in self._eval:
            eval(i)
        for i in self.allp:
            if i.id != self.player.id:
                i.draw(self.win, stage)
                i.drawname(self.win, stage)
        for i in self.allp:
            if i.id == self.player.id:
                self.player.update(self.dt)
                self.player.draw(self.win, stage)
                self.player.drawname(self.win, stage)
        pygame.display.update()
