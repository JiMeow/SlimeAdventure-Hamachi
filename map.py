import pygame
from src.setting import *
from src.obstacle.wall import Wall
from src.obstacle.spike import Spike
from src.obstacle.flyfloor import FlyingFloor
from src.obstacle.hedgehog import Hedgehog
from src.obstacle.jellyfish import Jellyfish
from src.powerup.jumpboost import Jumpboost
from src.powerup.invisible import Invisible
from src.stage.stage import *


class Map():
    def __init__(self, win, img, spawn) -> None:
        """
        set win and img to map

        Args:
            win (pygame.display): pygame window
            img (pygame.surface): map image
        """
        self.win = win
        self.spawneveryXstage = spawn
        self.img = pygame.transform.scale(
            pygame.image.load(img), (width, height))
        self.timeoffset = 0
        self.nowstage = -1
        self.gravity = 0.6
        self.obstacle = []
        self.spike = []
        self.flyfloor = []
        self.hedgehog = []
        self.jellyfish = []
        self.jumpboost = []
        self.invisible = []
        self.wall = []
        self.text = []
        self.stage = list(range(23))

    def reset(self):
        """
        reset all obstacle
        """
        self.obstacle = []
        self.spike = []
        self.flyfloor = []
        self.hedgehog = []
        self.jellyfish = []
        self.jumpboost = []
        self.invisible = []
        self.text = []
        self.wall = []

    def setobstacle(self):
        """
        set all obstacle by combine all obstacle
        """
        self.obstacle = self.spike + self.flyfloor + \
            self.hedgehog + self.jellyfish + self.jumpboost + self.invisible+self.wall

    def addflyfloor(self, x, y, stage):
        """
        add flying floor at (x,y) position to stage

        Args:
            x (int): x position of flying floor
            y (int): y position of flying floor
            stage (int): stage of game
        """
        self.flyfloor.append(FlyingFloor(
            self.win, x, y, stage))

    def addspike(self, x, y, stage, rotate=0):
        """
        add spike at (x,y) position to stage

        Args:
            x (int): x position of flying floor
            y (int): y position of flying floor
            stage (int): stage of game
        """
        self.spike.append(Spike(
            self.win, x, y, stage, rotate))

    def addhedgehog(self, x, y, stage, distance):
        """
        add hedgehog at (x,y) position to stage by walking time
        and maximum distance of hedgehog can walk

        Args:
            x (int): x position of hedgehog
            y (int): y position of hedgehog
            stage (int): stage of game
            distance (int): maximum distance of hedgehog can walk
        """
        self.hedgehog.append(Hedgehog(
            self.win, x, y, stage, distance, self.timeoffset))

    def addjellyfish(self, x, y, stage, distance):
        """
        add jellyfish at (x,y) position to stage by flying time
        and maximum distance of jellyfish can fly

        Args:
            x (int): x position of jellyfish
            y (int): y position of jellyfish
            stage (int): stage of game
            distance (int): maximum distance of jellyfish can flying
        """
        self.jellyfish.append(Jellyfish(
            self.win, x, y, stage, distance, self.timeoffset))

    def addjumpboost(self, x, y, stage):
        """
        add jumpboost at (x,y) position to stage

        Args:
            x (int): x position of jumpboost
            y (int): y position of jumpboost
            stage (int): stage of game
        """
        self.jumpboost.append(Jumpboost(
            self.win, x, y, stage))

    def addinvisible(self, x, y, stage):
        """
        add jumpboost at (x,y) position to stage

        Args:
            x (int): x position of jumpboost
            y (int): y position of jumpboost
            stage (int): stage of game
        """
        self.invisible.append(Invisible(
            self.win, x, y, stage))

    def addwall(self, x, y, stage, rotate=False):
        """
        add wall to stage

        Args:
            x (int): x position of wall
            y (int): y position of wall
            stage (int): stage of game
            rotate (bool): if rotate wall
        """
        self.wall.append(Wall(self.win, x, y, stage, rotate))

    def addtext(self, text, x, y, size, color="black"):
        """
        add text to stage

        Args:
            text (str): text to display
            x (int): x position of text
            y (int): y position of text
            size (int): size of text
        """
        font = pygame.font.Font(None, size)
        text = font.render(str(text), True, "black")
        textrect = text.get_rect(topleft=(x, y))
        self.text.append((text, textrect))

    def draw(self, stage):
        """
        draw map img to win and draw all component of stage

        Args:
            stage (int): stage of game
        """
        self.win.blit(self.img, (0, 0))
        if stage == self.nowstage:
            pass
        else:
            if stage in self.stage:
                try:
                    eval("createstage"+str(int(stage))+f"(self)")
                except:
                    eval("self.createstage"+str(int(stage))+f"()")
                self.nowstage = stage
                self.addtext(f"Stage: {int(stage)}", 10, 30, 20)
                if stage % self.spawneveryXstage == 0:
                    self.addtext("Checkpoint", 10, floor-50-40, 25)
        for i in self.obstacle:
            i.draw(stage)
        for i in self.text:
            self.win.blit(i[0], i[1])
