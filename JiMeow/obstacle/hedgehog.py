import pygame
from setting import *


class Hedgehog():

    def __init__(self, win, x, y, stage, time, distance):
        self.win = win
        self.img = pygame.transform.scale(
            pygame.image.load("JiMeow/photo/hedgehog.png"), (70, 50))
        self.width = 70
        self.height = 50
        self.x = x + width * stage
        self.y = y
        self.rect = pygame.Rect(self.x, y, 70, 50)
        self.speed = 1
        self.time = time % (distance*2) + 1
        self.distance = distance

    def draw(self, stage):
        self.update()
        self.win.blit(self.img, (self.x-width*stage, self.y))

    def walk(self):
        if self.time <= self.distance:
            self.x += self.speed * self.time
        else:
            self.img = pygame.transform.flip(self.img, True, False)
            self.x += self.speed * (self.distance*2-self.time)

    def update(self):
        self.walk()
        self.rect = pygame.Rect(self.x, self.y, 70, 50)
