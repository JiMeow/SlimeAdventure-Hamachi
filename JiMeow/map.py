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
        self.stage = list(range(6))

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
        stage = 0
        self.reset()
        for i in range(10):
            self.addflyfloor(500+45*i, floor-100, stage)
        for i in range(10):
            self.addflyfloor(950+45*i, floor-200, stage)
        for i in range(3):
            self.addhedgehog(400+75*i, floor, stage, 200)
        self.setobstacle()
        for i in self.obstacle:
            i.draw(stage)

    def stage1(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 1
        self.reset()

        for i in range(2):
            self.addflyfloor(45*i, floor-200, stage)
        for i in range(14):
            self.addspike(125+75*i, floor, stage)

        for i in range(2):
            self.addflyfloor(300+45*i, floor-300, stage)
        for i in range(2):
            self.addflyfloor(600+45*i, floor-400, stage)
        for i in range(2):
            self.addflyfloor(900+45*i, floor-500, stage)
        for i in range(2):
            self.addflyfloor(1200+45*i, floor-400, stage)

        self.setobstacle()
        for i in self.obstacle:
            i.draw(stage)

    def stage2(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 2
        self.reset()
        for i in range(14):
            self.addspike(125+75*i, floor, stage)

        for i in range(4):
            self.addflyfloor(200+45*i, floor-150, stage)
        self.addhedgehog(200, floor-200, stage, 120)

        for i in range(4):
            self.addflyfloor(500+45*i, floor-150, stage)
        self.addhedgehog(500, floor-200, stage, 120)

        for i in range(4):
            self.addflyfloor(800+45*i, floor-150, stage)
        self.addhedgehog(800, floor-200, stage, 120)

        self.setobstacle()
        for i in self.obstacle:
            i.draw(stage)

    def stage3(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 3
        self.reset()

        self.addhedgehog(150, floor, stage, 200)
        self.addhedgehog(350, floor, stage, 200)
        self.addhedgehog(550, floor, stage, 200)
        self.addhedgehog(750, floor, stage, 200)
        self.addhedgehog(950, floor, stage, 200)

        self.setobstacle()
        for i in self.obstacle:
            i.draw(stage)

    def stage4(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 4
        self.reset()

        for i in range(14):
            self.addspike(125+75*i, floor, stage)

        self.addflyfloor(200, floor-100, stage)
        self.addflyfloor(400, floor-250, stage)
        self.addflyfloor(600, floor-400, stage)
        self.addflyfloor(800, floor-550, stage)

        self.setobstacle()
        for i in self.obstacle:
            i.draw(stage)

    def stage5(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 5
        self.reset()
        for i in range(10):
            self.addflyfloor(500+45*i, floor-100, stage)
        for i in range(10):
            self.addflyfloor(950+45*i, floor-200, stage)
        for i in range(3):
            self.addhedgehog(400+75*i, floor, stage, 200)
        self.setobstacle()
        for i in self.obstacle:
            i.draw(stage)
