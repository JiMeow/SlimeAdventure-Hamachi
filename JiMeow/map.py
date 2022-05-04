import pygame
import time
from setting import *
from obstacle.spike import Spike
from obstacle.flyfloor import FlyingFloor
from obstacle.hedgehog import Hedgehog
from obstacle.jellyfish import Jellyfish
from powerup.jumpboost import Jumpboost


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
        self.nowstage = -1
        self.gravity = 0.3
        self.obstacle = []
        self.spike = []
        self.flyfloor = []
        self.hedgehog = []
        self.jellyfish = []
        self.jumpboost = []
        self.text = []
        self.stage = list(range(10))

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
        self.text = []

    def setobstacle(self):
        """
        set all obstacle by combine all obstacle
        """
        self.obstacle = self.spike + self.flyfloor + \
            self.hedgehog + self.jellyfish + self.jumpboost

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
            self.win, x, y, stage, distance))

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
            self.win, x, y, stage, distance))

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
                eval("self.createstage"+str(int(stage))+f"()")
                self.nowstage = stage

        for i in self.obstacle:
            i.draw(stage)
        for i in self.text:
            self.win.blit(i[0], i[1])

    def createstage0(self):
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

    def createstage1(self):
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

    def createstage2(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 2
        self.reset()

        for i in range(14):
            self.addspike(125+75*i, floor, stage)
        self.addflyfloor(200, floor-100, stage)
        self.addflyfloor(400, floor-250, stage)
        self.addflyfloor(600, floor-400, stage)
        self.addflyfloor(800, floor-550, stage)
        self.setobstacle()

    def createstage3(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 3
        self.reset()

        for i in range(14):
            self.addspike(125+75*i, floor, stage)
        for i in range(4):
            self.addflyfloor(200+45*i, floor-150, stage)
        self.addhedgehog(200, floor-200, stage, 180)
        for i in range(4):
            self.addflyfloor(500+45*i, floor-150, stage)
        self.addhedgehog(500, floor-200, stage, 180)
        for i in range(4):
            self.addflyfloor(800+45*i, floor-150, stage)
        self.addhedgehog(800, floor-200, stage, 180)
        self.setobstacle()

    def createstage4(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 4
        self.reset()

        self.addhedgehog(150, floor, stage, 200)
        self.addhedgehog(350, floor, stage, 200)
        self.addhedgehog(550, floor, stage, 200)
        self.addhedgehog(750, floor, stage, 200)
        self.addhedgehog(950, floor, stage, 200)
        self.setobstacle()

    def createstage5(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 5
        self.reset()

        for i in range(14):
            self.addspike(125+75*i, floor, stage)
        for i in range(16):
            self.addflyfloor(335+45*i, floor-300, stage)
        for i in range(5):
            self.addflyfloor(50+50*(i+1), floor-100-50*i, stage)
        for i in range(4):
            self.addflyfloor(1005+50*(i+1), floor-250+50*i, stage)
        self.addjellyfish(200, floor-400, stage, 300)
        self.addjellyfish(400, floor-600, stage, 500)
        self.addjellyfish(600, floor-500, stage, 400)
        self.addjellyfish(800, floor-300, stage, 200)
        self.addjellyfish(1000, floor-500, stage, 200)
        self.addtext("Checkpoint", 10, floor-40, 25)
        self.setobstacle()

    def createstage6(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 6
        self.reset()

        self.addjumpboost(600, floor-200, stage)
        self.addtext("Jump?", 600, floor-225, 24)
        self.setobstacle()

    def createstage7(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 7
        self.reset()

        self.addjumpboost(250, floor-200, stage)
        self.addjumpboost(550, floor-200, stage)
        self.addjumpboost(850, floor-200, stage)
        for i in range(13):
            self.addspike(175+75*i, floor, stage)
        self.setobstacle()

    def createstage8(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 8
        self.reset()

        self.addjellyfish(200, floor-400, stage, 400)
        self.addjellyfish(350, floor-500, stage, 500)
        self.addjellyfish(500, floor-100, stage, 100)
        self.addjellyfish(650, floor-200, stage, 200)
        self.addjellyfish(800, floor-400, stage, 400)
        self.addjellyfish(950, floor-200, stage, 200)
        self.addjellyfish(1100, floor-600, stage, 600)
        self.setobstacle()
