import pygame
from src.setting import *
from src.obstacle.wall import Wall
from src.powerup.jumpboost import Jumpboost
from src.obstacle.spike import Spike
from src.obstacle.flyfloor import FlyingFloor
from src.obstacle.hedgehog import Hedgehog
from src.obstacle.jellyfish import Jellyfish


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
        self.timeoffset = 0
        self.nowstage = -1
        self.gravity = 0.3
        self.obstacle = []
        self.spike = []
        self.flyfloor = []
        self.hedgehog = []
        self.jellyfish = []
        self.jumpboost = []
        self.wall = []
        self.text = []
        self.stage = list(range(21))

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
        self.wall = []

    def setobstacle(self):
        """
        set all obstacle by combine all obstacle
        """
        self.obstacle = self.spike + self.flyfloor + \
            self.hedgehog + self.jellyfish + self.jumpboost + self.wall

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
            self.addflyfloor(500+45*i, floor-50-100, stage)
        for i in range(10):
            self.addflyfloor(950+45*i, floor-50-200, stage)
        for i in range(3):
            self.addhedgehog(400+75*i, floor-50, stage, 200)
        self.setobstacle()

    def createstage1(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 1
        self.reset()

        for i in range(2):
            self.addflyfloor(45*i, floor-50-200, stage)
        for i in range(14):
            self.addspike(125+75*i, floor-50, stage)
        for i in range(2):
            self.addflyfloor(300+45*i, floor-50-300, stage)
        for i in range(2):
            self.addflyfloor(600+45*i, floor-50-400, stage)
        for i in range(2):
            self.addflyfloor(900+45*i, floor-50-500, stage)
        for i in range(2):
            self.addflyfloor(1200+45*i, floor-50-400, stage)
        self.setobstacle()

    def createstage2(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 2
        self.reset()

        for i in range(14):
            self.addspike(125+75*i, floor-50, stage)
        self.addflyfloor(200, floor-50-100, stage)
        self.addflyfloor(400, floor-50-250, stage)
        self.addflyfloor(600, floor-50-400, stage)
        self.addflyfloor(800, floor-50-550, stage)
        self.setobstacle()

    def createstage3(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 3
        self.reset()

        for i in range(14):
            self.addspike(125+75*i, floor-50, stage)
        for i in range(4):
            self.addflyfloor(200+45*i, floor-50-150, stage)
        self.addhedgehog(200, floor-50-200, stage, 180)
        for i in range(4):
            self.addflyfloor(500+45*i, floor-50-150, stage)
        self.addhedgehog(500, floor-50-200, stage, 180)
        for i in range(4):
            self.addflyfloor(800+45*i, floor-50-150, stage)
        self.addhedgehog(800, floor-50-200, stage, 180)
        self.setobstacle()

    def createstage4(self):
        """
        reset all obstacle then add new obstacle to stage 1
        then draw this stage
        """
        stage = 4
        self.reset()

        self.addhedgehog(150, floor-50, stage, 200)
        self.addhedgehog(350, floor-50, stage, 200)
        self.addhedgehog(550, floor-50, stage, 200)
        self.addhedgehog(750, floor-50, stage, 200)
        self.addhedgehog(950, floor-50, stage, 200)
        self.setobstacle()

    def createstage5(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 5
        self.reset()

        for i in range(14):
            self.addspike(125+75*i, floor-50, stage)
        for i in range(16):
            self.addflyfloor(335+45*i, floor-50-300, stage)
        for i in range(5):
            self.addflyfloor(50+50*(i+1), floor-50-100-50*i, stage)
        for i in range(4):
            self.addflyfloor(1005+50*(i+1), floor-50-250+50*i, stage)
        self.addjellyfish(200, floor-50-400, stage, 300)
        self.addjellyfish(400, floor-50-600, stage, 500)
        self.addjellyfish(600, floor-50-500, stage, 400)
        self.addjellyfish(800, floor-50-300, stage, 200)
        self.addjellyfish(1000, floor-50-500, stage, 200)
        self.addtext("Checkpoint", 10, floor-50-40, 25)
        self.setobstacle()

    def createstage6(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 6
        self.reset()

        self.addjumpboost(600, floor-50-200, stage)
        self.addtext("Jump?", 600, floor-50-225, 24)
        self.setobstacle()

    def createstage7(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 7
        self.reset()

        self.addjumpboost(250, floor-50-200, stage)
        self.addjumpboost(550, floor-50-200, stage)
        self.addjumpboost(850, floor-50-200, stage)
        for i in range(13):
            self.addspike(175+75*i, floor-50, stage)
        self.setobstacle()

    def createstage8(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 8
        self.reset()

        self.addjellyfish(200, floor-50-400, stage, 400)
        self.addjellyfish(350, floor-50-500, stage, 500)
        self.addjellyfish(500, floor-50-100, stage, 100)
        self.addjellyfish(650, floor-50-200, stage, 200)
        self.addjellyfish(800, floor-50-400, stage, 400)
        self.addjellyfish(950, floor-50-200, stage, 200)
        self.addjellyfish(1100, floor-50-600, stage, 600)
        self.setobstacle()

    def createstage9(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 9
        self.reset()

        for i in range(13):
            self.addspike(200+71.25*i, floor-50, stage)
        for i in range(20):
            self.addflyfloor(200+45*i, floor-200, stage)
        self.addhedgehog(400, floor-50-200, stage, 200)
        self.addhedgehog(700, floor-50-200, stage, 200)

        for i in range(20):
            self.addflyfloor(200+45*i, floor-400, stage)
        self.addhedgehog(250, floor-50-400, stage, 200)
        self.addhedgehog(550, floor-50-400, stage, 200)
        self.addhedgehog(850, floor-50-400, stage, 200)

        for i in range(20):
            self.addflyfloor(200+45*i, floor-600, stage)
        for i in range(13):
            self.addspike(200+71.25*i, floor-600+15, stage, 180)
        self.setobstacle()

    def createstage10(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 10
        self.reset()

        self.addjumpboost(200, floor-50-200, stage)
        for i in range(13):
            self.addspike(200+71.25*i, floor-50, stage)
        for i in range(4):
            self.addflyfloor(500+45*i, floor-50-150, stage)
        self.addhedgehog(500, floor-50-200, stage, 180)
        for i in range(4):
            self.addflyfloor(800+45*i, floor-50-150, stage)
        self.addhedgehog(800, floor-50-200, stage, 180)
        self.addtext("Checkpoint", 10, floor-50-40, 25)
        self.setobstacle()

    def createstage11(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 11
        self.reset()

        for i in range(13):
            self.addspike(200+71.25*i, floor-50, stage)
        self.addjumpboost(200, floor-50-200, stage)
        self.addjellyfish(350, floor-50-350, stage, 200)
        self.addjumpboost(500, floor-50-200, stage)
        self.addjellyfish(650, floor-50-350, stage, 200)
        self.addjumpboost(800, floor-50-200, stage)
        self.addjellyfish(950, floor-50-350, stage, 200)
        self.setobstacle()

    def createstage12(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 12
        self.reset()

        for i in range(3):
            self.addspike(200+60*i, floor-50, stage)

        for i in range(3):
            self.addspike(450+60*i, floor-50, stage)

        for i in range(3):
            self.addspike(700+60*i, floor-50, stage)

        for i in range(3):
            self.addspike(950+60*i, floor-50, stage)
        self.setobstacle()

    def createstage13(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 13
        self.reset()
        self.addhedgehog(200, floor-50, stage, 300)
        self.addhedgehog(500, floor-50, stage, 300)
        self.addhedgehog(800, floor-50, stage, 300)
        self.addjellyfish(350, floor-50-300, stage, 300)
        self.addjellyfish(650, floor-50-300, stage, 200)
        self.addjellyfish(950, floor-50-200, stage, 150)
        self.setobstacle()

    def createstage14(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 14
        self.reset()
        for i in range(4):
            self.addwall(200, floor-90-85*i, stage)
        self.addwall(200, floor-390, stage, rotate=True)
        for i in range(9):
            self.addwall(400+85*i, floor-390, stage, rotate=True)
        self.addflyfloor(155, floor-195, stage)
        self.addflyfloor(155, floor-390, stage)
        for i in range(3):
            self.addhedgehog(500+200*i, floor-50-390, stage, 200)
        for i in range(12):
            self.addspike(300+75*i, floor-50, stage)
        for i in range(10):
            self.addspike(410+75*i, floor-340, stage, 180)
        self.addjumpboost(600, floor-200, stage)
        self.addjellyfish(750, floor-300, stage, 200)
        self.addjumpboost(900, floor-200, stage)
        self.setobstacle()

    def createstage15(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 15
        self.reset()

        for i in range(6):
            self.addwall(100, floor-200-85*i, stage)
        for i in range(7):
            self.addwall(100+85*i, floor-600-75, stage, rotate=True)
        for i in range(6):
            self.addspike(100+85*i, floor-600-25, stage, 180)
        for i in range(6):
            self.addwall(300, floor-90-85*i, stage)
        self.addwall(350, floor-515, stage, rotate=True)
        for i in range(6):
            self.addwall(435, floor-90-85*i, stage)
        self.addflyfloor(150, floor-125, stage)
        self.addflyfloor(255, floor-280, stage)
        self.addflyfloor(150, floor-435, stage)
        for i in range(6):
            self.addwall(645, floor-200-85*i, stage)
        self.addspike(645-48, floor-475-25, stage, 270)
        self.addspike(645-48, floor-400-25, stage, 270)
        self.addspike(645-48, floor-325-25, stage, 270)
        self.addspike(490, floor-225-25, stage, 90)
        self.addspike(490, floor-150-25, stage, 90)
        self.addspike(490, floor-75-25, stage, 90)
        for i in range(7):
            self.addwall(697+85*i, 527, stage, True)
        self.addjellyfish(750, floor-120, stage, 100)
        self.addspike(900, floor-50, stage, 0)
        self.addspike(975, floor-110, stage, 180)
        self.addspike(1050, floor-50, stage, 0)
        self.addspike(1125, floor-110, stage, 180)
        self.setobstacle()

    def createstage16(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 16
        self.reset()
        for i in range(5):
            self.addwall(200, floor-90-85*i, stage)
        self.addwall(200, floor-480, stage, rotate=True)
        for i in range(3):
            self.addflyfloor(155, floor-160*(i+1), stage)
        for i in range(8):
            self.addhedgehog(250+100*i, floor-50, stage, 100)
        self.addjumpboost(370, floor-400, stage)
        self.addjumpboost(670, floor-400, stage)
        self.addjumpboost(950, floor-400, stage)
        self.addjumpboost(370, floor-250, stage)
        self.addjumpboost(670, floor-250, stage)
        self.addjumpboost(950, floor-250, stage)
        for i in range(5):
            self.addwall(1090, floor-90-85*i, stage)
        self.addwall(1055, floor-480, stage, rotate=True)
        for i in range(3):
            self.addflyfloor(1145, floor-160*(i+1), stage)
        self.addjellyfish(520, floor-500, stage, 200)
        self.addjellyfish(520, floor-500, stage, 350)
        self.addjellyfish(820, floor-500, stage, 250)
        self.addjellyfish(820, floor-500, stage, 300)
        # self.addjellyfish(20, floor-600, stage, 500)
        self.setobstacle()

    def createstage17(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 17
        self.reset()

        self.setobstacle()

    def createstage18(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 18
        self.reset()

        self.setobstacle()

    def createstage19(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 19
        self.reset()

        self.setobstacle()

    def createstage20(self):
        """
        reset all obstacle then add new obstacle to stage 0 
        then draw this stage
        """
        stage = 20
        self.reset()

        self.setobstacle()
