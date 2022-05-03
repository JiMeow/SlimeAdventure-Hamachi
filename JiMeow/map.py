import pygame
import time
from setting import *
from obstacle.spike import Spike
from obstacle.flyfloor import FlyingFloor
from obstacle.hedgehog import Hedgehog


class Map():
    def __init__(self, win, img) -> None:
        """
        set win and img to map

        Args:
            win (pygame.display): pygame window
            img (pygame.surface): map image
        """
        self.win = win
        self.img = pygame.transform.scale(
            pygame.image.load(img), (width, height))
        self.gravity = 0.3
        self.obstacle = []
        self.spike = []
        self.flyfloor = []
        self.hedgehog = []
        self.stage = list(range(2))

    def reset(self):
        """
        reset all obstacle
        """
        self.obstacle = []
        self.spike = []
        self.flyfloor = []
        self.hedgehog = []

    def setobstacle(self):
        """
        set all obstacle by combine all obstacle
        """
        self.obstacle = self.spike + self.flyfloor + self.hedgehog

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

    def addspike(self, x, y, stage):
        """
        add spike at (x,y) position to stage

        Args:
            x (int): x position of flying floor
            y (int): y position of flying floor
            stage (int): stage of game
        """
        self.spike.append(Spike(
            self.win, x, y, stage))

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
            self.win, x, y, stage, int(time.time()*100), distance))

    def draw(self, stage):
        """
        draw map img to win and draw all component of stage

        Args:
            stage (int): stage of game
        """
        self.win.blit(self.img, (0, 0))
        if stage in self.stage:
            eval("self.stage"+str(int(stage))+f"()")

    def stage0(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        self.reset()
        for i in range(10):
            self.addflyfloor(500+45*i, floor-100, 0)
        for i in range(10):
            self.addflyfloor(950+45*i, floor-200, 0)
        self.addhedgehog(400, floor, 0, 200)
        self.addhedgehog(470, floor, 0, 200)
        self.setobstacle()
        for i in self.obstacle:
            i.draw(0)

    def stage1(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        self.reset()
        for i in range(2):
            self.addflyfloor(45*i, floor-200, 1)
        for i in range(20):
            self.addflyfloor(45*i, floor-300, 1)
        for i in range(10):
            self.addspike(200+70*i, floor+2, 1)
        self.setobstacle()
        for i in self.obstacle:
            i.draw(1)
