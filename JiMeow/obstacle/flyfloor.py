import pygame
from setting import *


class FlyingFloor():

    def __init__(self, win, x, y, stage):
        """
        set default value of flying floor depend on stage

        Args:
            win (pygame.display): pygame window
            x (int): x position of flying floor
            y (int): y position of flying floor
            stage (int): stage of game
        """
        self.win = win
        self.img = pygame.transform.scale(
            pygame.image.load("JiMeow/photo/flyfloor.png"), (45, 15))
        self.weight = 45
        self.height = 15
        self.x = x + width*stage
        self.y = y
        self.rect = pygame.Rect(self.x, y, 45, 15)

    def draw(self, stage):
        """
        draw flying floor img at stage by rect

        Args:
            stage (int): stage of game #can change to self.stage 
        """
        self.win.blit(self.img, (self.x-width*stage, self.y))
