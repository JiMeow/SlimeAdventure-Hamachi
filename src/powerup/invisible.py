import pygame
from src.setting import *


class Invisible():

    img = pygame.transform.scale(
        pygame.image.load("src/photo/invisible.png"), (50, 50))

    def __init__(self, win, x, y, stage):
        """
        set default value of uni depend on stage

        Args:
            win (pygame.display): pygame window
            x (int): x position of uni
            y (int): y position of uni
            stage (int): stage of game
        """
        self.win = win
        self.width = 50
        self.height = 50
        self.x = x + width * stage
        self.y = y
        self.rect = pygame.Rect(self.x+5, y+5, self.width-5, self.height-5)
        self.use = False
        self.timedelay = 120

    def draw(self, stage):
        """
        update position of uni and draw uni at stage by rect

        Args:
            stage (int): stage of game
        """
        if not self.use:
            self.win.blit(Invisible.img, (self.x-width*stage, self.y))
        else:
            self.update()

    def used(self):
        """
        update is item was used or not and change position of uni
        """
        self.use = True
        self.rect = pygame.Rect(self.x+5, self.y-1000,
                                self.width-5, self.height-5)

    def update(self):
        """
        change time count when uni is used for a while
        then change position of uni to default and show uni again
        """
        if self.timedelay == 0:
            self.timedelay = 240
            self.rect = pygame.Rect(
                self.x+5, self.y+5, self.width-5, self.height-5)
            self.use = False
        else:
            self.timedelay -= 1
