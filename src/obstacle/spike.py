import pygame
from src.setting import *


class Spike():

    imgup = pygame.transform.scale(
        pygame.image.load("src/photo/spike.png"), (40, 50))
    imgright = pygame.transform.rotate(imgup, 90)
    imgdown = pygame.transform.rotate(imgright, 90)
    imgleft = pygame.transform.rotate(imgdown, 90)

    def __init__(self, win, x, y, stage, rotate=0):
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
        self.rotate = rotate
        if self.rotate == 0:
            self.hitbox = [
                pygame.Rect(self.x+3, y+40, 35, 10),
                pygame.Rect(self.x+6, y+35, 28, 5),
                pygame.Rect(self.x+9, y+30, 22, 5),
                pygame.Rect(self.x+12, y+25, 16, 5),
                pygame.Rect(self.x+15, y+10, 10, 15),
            ]
        elif self.rotate == 180:
            self.hitbox = [
                pygame.Rect(self.x+3, y+2, 35, 10),
                pygame.Rect(self.x+6, y+12, 28, 5),
                pygame.Rect(self.x+9, y+17, 22, 5),
                pygame.Rect(self.x+12, y+22, 16, 5),
                pygame.Rect(self.x+16, y+27, 10, 15),
            ]
        elif self.rotate == 90:
            self.hitbox = [
                pygame.Rect(self.x, y+3, 10, 35),
                pygame.Rect(self.x+10, y+6, 5, 28),
                pygame.Rect(self.x+15, y+9, 5, 22),
                pygame.Rect(self.x+20, y+12, 5, 16),
                pygame.Rect(self.x+25, y+15, 15, 10),
            ]
        elif self.rotate == 270:
            self.hitbox = [
                pygame.Rect(self.x+35, y+3, 15, 35),
                pygame.Rect(self.x+30, y+6, 5, 28),
                pygame.Rect(self.x+25, y+9, 5, 22),
                pygame.Rect(self.x+20, y+12, 5, 16),
                pygame.Rect(self.x+10, y+15, 10, 10),
            ]

    def draw(self, stage):
        """
         draw spike at stage by rect

        Args:
            stage (int): stage of game #can change to self.stage
        """
        if self.rotate == 0:
            self.win.blit(Spike.imgup, (self.x-width*stage, self.y))
        if self.rotate == 180:
            self.win.blit(Spike.imgdown, (self.x-width*stage, self.y))
        if self.rotate == 90:
            self.win.blit(Spike.imgleft, (self.x-width*stage, self.y))
        if self.rotate == 270:
            self.win.blit(Spike.imgright, (self.x-width*stage, self.y))
