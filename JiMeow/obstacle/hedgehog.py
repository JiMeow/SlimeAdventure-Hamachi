import pygame
from setting import *
import time


class Hedgehog():

    img = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/hedgehog.png"), (70, 50))
    imgflip = pygame.transform.flip(img, True, False)
    img = [img, imgflip]

    def __init__(self, win, x, y, stage, distance, timeoffset):
        """
        set default value of flying floor depend on stage

        Args:
            win (pygame.display): pygame window
            x (int): x position of flying floor
            y (int): y position of flying floor
            stage (int): stage of game
            time (int): now time.time()*100 for generate position of hedgehog walk
            distance (int): distance of hedgehog will walk then turnback
        """
        self.win = win
        self.width = 70
        self.height = 50
        self.x = x + width * stage
        self.constx = self.x
        self.y = y
        self.distance = distance*2//3
        self.speed = 1
        self.timeoffset = timeoffset

    def draw(self, stage):
        """
        update position of hedgehog and draw hedgehog at stage by rect

        Args:
            stage (int): stage of game #can change to self.stage
        """
        imgindex = self.walk()
        self.update()
        self.win.blit(Hedgehog.img[imgindex], (self.x-width*stage, self.y))

    def walk(self):
        """
        hedgehog walk to left or right depend on time

        Returns:
            int: 1 for walk to left, 0 for walk to right
        """
        self.settime()
        self.x = self.constx + (int((time.time()-self.timeoffset)*100) *
                                self.speed) % (self.distance*2)
        if self.x > self.constx + self.distance:
            self.x = self.constx + self.distance - \
                (self.x-(self.constx + self.distance))
            return 1
        return 0

    def update(self):
        """
        hedgehog walk and set new rect of hedgehog
        """
        self.rect = pygame.Rect(
            self.x+5, self.y+5, self.width-5, self.height-5)

    def settime(self):
        """
        set time for set position of hedgehog
        """
        self.time = int(time.time()*100) % (self.distance*2) + 1
