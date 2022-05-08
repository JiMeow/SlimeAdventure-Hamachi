from platform import platform
import pygame
from src.setting import *


class Layout():
    def __init__(self, win):
        """
        set default value of layout for setting draw layer

        Args:
            win (pygame.display): pygame window
        """
        self.win = win
        self.dt = 1/60

    def setPlayer(self, player):
        """
        set player information to layout

        Args:
            player (Player): player who play client information
        """
        self.player = player

    def setPlayerStatus(self, status):
        '''This function sets the status of the player to the status passed in as a parameter

        Parameters
        ----------
        status
            The status of the player.

        '''
        self.status = status

    def setAllPlayer(self, player):
        """
        set all player information to layout

        Args:
            player (List[Player]): list infomation of all player
        """
        self.allp = player

    def setMap(self, map):
        """
        set map information to layout

        Args:
            map (Map): map information
        """
        self.map = map

    def setDt(self, dt):
        """
        set delta time to layout

        Args:
            dt (float): delta time check for lag
        """
        self.dt = dt

    def setCollision(self, collision):
        """
        set collision information to layout

        Args:
            collision (Collision): collision information
        """
        self.collision = collision

    def setDebug(self, info, x, y, color="White"):
        """
        debug for show information on screen

        Args:
            info (str): text to show
            x (int): x position of text
            y (int): y position of text
        """
        font = pygame.font.Font(None, 20)
        self.text = font.render(str(info), True, color)
        self.textrect = self.text.get_rect(topleft=(x, y))

    def drawDeathcount(self):
        deathcount = []
        for player in self.allp:
            if self.status[player.id-1] == 1:
                deathcount.append(
                    (-int(player.x//width), -player.difficulty, player.deathcount, player.name))
        deathcount.sort()
        font = pygame.font.Font(None, 20)
        number = 0
        # print(deathcount)
        for stage, difficulty, death, name in deathcount:
            stage = -stage
            difficulty = -difficulty
            self.stagetext = font.render("["+str(stage)+"]", True, "Black")
            self.stagetextrect = self.stagetext.get_rect(
                topleft=(1150, 10+number*30))
            self.win.blit(self.stagetext, self.stagetextrect)
            if difficulty == 1:
                self.nametext = font.render(str(name), True, "Green")
                self.nametextrect = self.nametext.get_rect(
                    topleft=(1180, 10+number*30))
                self.win.blit(self.nametext, self.nametextrect)
            if difficulty == 5:
                self.nametext = font.render(str(name), True, "Blue")
                self.nametextrect = self.nametext.get_rect(
                    topleft=(1180, 10+number*30))
                self.win.blit(self.nametext, self.nametextrect)
            if difficulty == 10:
                self.nametext = font.render(str(name), True, "Black")
                self.nametextrect = self.nametext.get_rect(
                    topleft=(1180, 10+number*30))
                self.win.blit(self.nametext, self.nametextrect)
            if difficulty == 30:
                self.nametext = font.render(str(name), True, "Red")
                self.nametextrect = self.nametext.get_rect(
                    topleft=(1180, 10+number*30))
                self.win.blit(self.nametext, self.nametextrect)
            self.colontext = font.render(':', True, "White")
            self.colontextrect = self.colontext.get_rect(
                topleft=(1260, 10+number*30))
            self.win.blit(self.colontext, self.colontextrect)
            self.deadtext = font.render(
                (4-len(str(death)))*" " + str(death), True, "White")
            self.deadtextrect = self.deadtext.get_rect(
                topleft=(1270, 10+number*30))
            self.win.blit(self.deadtext, self.deadtextrect)
            number += 1

    def drawPlayerFrame(self):
        """
        calculate stage by position of player and draw stage that player in 
        then draw another player then set player information for collision
        update player information and draw player 
        """
        stage = self.player.x//width
        self.map.draw(stage)
        for i in self.allp:
            if i.id != self.player.id:
                i.draw(self.win, stage)
                i.drawname(self.win, stage)

        self.player.draw(self.win, stage)
        self.player.drawname(self.win, stage)

        # debug
        self.win.blit(self.text, self.textrect)
        self.drawDeathcount()
        pygame.display.update()
