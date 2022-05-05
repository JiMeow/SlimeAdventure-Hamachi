import pygame
from setting import *


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

    def setDebug(self, info, x, y):
        """
        debug for show information on screen

        Args:
            info (str): text to show
            x (int): x position of text
            y (int): y position of text
        """
        font = pygame.font.Font(None, 20)
        self.text = font.render(str(info), True, "White")
        self.textrect = self.text.get_rect(topleft=(x, y))

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
        for i in self.allp:
            if i.id == self.player.id:
                self.collision.setPlayer(i)
                self.player.update(self.dt, self.collision)
                self.player.draw(self.win, stage)
                self.player.drawname(self.win, stage)

        # debug
        self.win.blit(self.text, self.textrect)
        pygame.display.update()
