import pygame
from setting import *


class Hedgehog():

    img = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/hedgehog.png"), (70, 50))
    imgflip = pygame.transform.flip(img, True, False)
    img = [img, imgflip]

    def __init__(self, win, x, y, stage, time, distance):
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
        self.y = y
        self.rect = pygame.Rect(self.x, y, 70, 50)
        self.speed = 1
        self.time = time % (distance*2) + 1
        self.distance = distance

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
            int: 1 for walk to left, -1 for walk to right
        """
        if self.time <= self.distance:
            self.x += self.speed * self.time
            return 0  # 0 means hedgehog walk to left
        else:
            self.x += self.speed * (self.distance*2-self.time)
            return 1  # 1 means hedgehog walk to right

    def update(self):
        """
        hedgehog walk and set new rect of hedgehog
        """
        self.rect = pygame.Rect(self.x, self.y, 70, 50)
