import pygame
from setting import *


class Spike():

    img = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/spike.png"), (40, 50))

    def __init__(self, win, x, y, stage):
        """
        set default value of spike depend on stage

        Args:
            win (pygame.display): pygame window
            x (int): x position of spike
            y (int): y position of spike
            stage (int): stage of game
        """
        self.win = win
        self.width = 40
        self.height = 50
        self.x = x + width * stage
        self.y = y
        self.rect = pygame.Rect(self.x, y, 40, 50)

    def draw(self, stage):
        """
         draw spike at stage by rect

        Args:
            stage (int): stage of game #can change to self.stage
        """
        self.win.blit(Spike.img, (self.x-width*stage, self.y))
