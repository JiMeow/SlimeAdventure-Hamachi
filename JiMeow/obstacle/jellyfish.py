import pygame
from setting import *
import time


class Jellyfish():

    img1 = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/jellyfish1.png"), (40, 45))
    img2 = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/jellyfish2.png"), (53, 45))
    img3 = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/jellyfish3.png"), (60, 40))

    def __init__(self, win, x, y, stage, distance):
        """
        set default value of flying floor depend on stage

        Args:
            win (pygame.display): pygame window
            x (int): x position of flying floor
            y (int): y position of flying floor
            stage (int): stage of game
            time (int): now time.time()*100 for generate position of jellyfish walk
            distance (int): distance of jellyfish will walk then turnback
        """
        self.distance = distance
        self.win = win
        self.x = x + width * stage
        self.y = y
        self.speed = 1
        self.consty = y

    def draw(self, stage):
        """
        update position of jellyfish and draw jellyfish at stage by rect

        Args:
            stage (int): stage of game #can change to self.stage
        """
        self.update()
        if self.animation == 0:
            self.win.blit(Jellyfish.img1, (self.x-width*stage, self.y))
        if self.animation == 1:
            self.win.blit(Jellyfish.img2, (self.x-width*stage-6, self.y))
        if self.animation == 2:
            self.win.blit(Jellyfish.img3, (self.x-width*stage-10, self.y))

    def walk(self):
        """
        jellyfish walk to up or down depend on time
        """
        self.y = self.consty + (int(time.time()*100) *
                                self.speed) % (self.distance*2)
        if self.y > self.consty + self.distance:
            self.y = self.consty + self.distance - \
                (self.y-(self.consty + self.distance))

    def update(self):
        """
        set animation for jellyfish, jellyfish walk 
        and set new rect of jellyfish
        """
        self.setanimation()
        self.walk()
        if self.animation == 0:
            self.width = 40
            self.height = 45
            self.rect = pygame.Rect(
                self.x+5, self.y+5, self.width-5, self.height-5)
        if self.animation == 1:
            self.width = 53
            self.height = 45
            self.rect = pygame.Rect(
                self.x+5-6, self.y+5, self.width-5, self.height-5)
        if self.animation == 2:
            self.width = 60
            self.height = 40
            self.rect = pygame.Rect(
                self.x+5-10, self.y+5, self.width-5, self.height-5)

    def settime(self):
        """
        set time for set position of jellyfish
        """
        self.time = int(time.time()*100) % (self.distance*2)

    def setanimation(self):
        """
        set 
        """
        self.settime()
        self.animation = self.time//33 % 3
