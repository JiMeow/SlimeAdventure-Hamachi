import pygame
from src.setting import *


class Wall():

    imgvertical = pygame.transform.scale(
        pygame.image.load("src/photo/wall.png"), (55, 90))
    imghorizon = pygame.transform.rotate(imgvertical, 90)

    def __init__(self, win, x, y, stage, rotate=False):
        """
        set default value of wall depend on stage

        Args:
            win (pygame.display): pygame window
            x (int): x position of spike
            y (int): y position of spike
            stage (int): stage of game
            rotate (bool): if rotate wall
        """
        self.win = win
        self.width = 55
        self.height = 90
        self.x = x + width * stage
        self.y = y
        self.rotate = rotate
        if not rotate:
            self.rect = pygame.Rect(self.x, y, 55, 90)
        else:
            self.rect = pygame.Rect(self.x, y, 90, 55)

    def draw(self, stage):
        """
         draw spike at stage by rect

        Args:
            stage (int): stage of game #can change to self.stage
        """
        # draw hitbox of spike
        if not self.rotate:
            self.win.blit(Wall.imgvertical, (self.x-width*stage, self.y))
        else:
            self.win.blit(Wall.imghorizon, (self.x-width*stage, self.y))
