import pygame
from src.setting import *


class Spike():

    img = pygame.transform.scale(
        pygame.image.load("src/photo/spike.png"), (40, 50))
    imgflip = pygame.transform.flip(img, False, True)

    def __init__(self, win, x, y, stage, flip=False):
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
        self.flip = flip
        self.rect = pygame.Rect(self.x, y, 40, 50)
        self.hitbox = [
            pygame.Rect(self.x+3, y+40, 35, 10),
            pygame.Rect(self.x+6, y+35, 28, 5),
            pygame.Rect(self.x+9, y+30, 22, 5),
            pygame.Rect(self.x+12, y+25, 16, 5),
            pygame.Rect(self.x+15, y+10, 10, 15),
        ]

    def draw(self, stage):
        """
         draw spike at stage by rect

        Args:
            stage (int): stage of game #can change to self.stage
        """
        # draw hitbox of spike
        if not self.flip:
            self.win.blit(Spike.img, (self.x-width*stage, self.y))
        else:
            self.win.blit(Spike.imgflip, (self.x-width*stage, self.y))
