import pygame
from setting import *


class Collision():
    def __init__(self, p, allp, map, spawnstage):
        """
        set player, all player, and map to the class

        Args:
            p (Player): infomation of player who play client
            allp (List[Player]): list infomation of all player
            map (Map): map information
        """
        self.player = p
        self.allp = allp
        self.map = map
        self.spawnstage = spawnstage

    def setAllPlayer(self, allp):
        """
        set all player to the class

        Args:
            allp (List[Player]): list infomation of all player
        """
        self.allp = allp

    def setPlayerX(self, x):
        """
        set position_x of player to the class

        Args:
            x (int): x position of player
        """
        self.player.x = x

    def setPlayerY(self, y):
        """
        set position_y of player to the class

        Args:
            y (int): y position of player
        """
        self.player.y = y

    def setPlayerXY(self, x, y):
        """
        set position_x and position_y of player to the class

        Args:
            x (int): x position of player
            y (int): y position of player
        """
        self.setPlayerX(x)
        self.setPlayerY(y)

    def setMap(self, map):
        """
        set map information to the class

        Args:
            map (Map): map information
        """
        self.map = map

    def setPlayer(self, player):
        """
        set player informmation to the class

        Args:
            player (Player): infomation of player who play client
        """
        self.player = player

    def setSpawnStage(self, spawnstage):
        """
        set spawn stage to the class

        Args:
            spawnstage (int): spawn stage
        """
        self.spawnstage = spawnstage

    def playerCollideFloor(self):
        """
        check if player collide with floor or not and return the result

        Returns:
            bool: True if player collide with floor, False if not
            tuple: position of player after collision
        """
        if self.player.y >= floor:
            return True, (self.player.x, floor)
        return False, None

    def playerCollideFlyingFloor(self):
        """
        check if player(foot) collide with flying floor or not and return the result

        Returns:
            bool: True if player collide with flying floor, False if not
            tuple: position of player after collision
        """
        for i in self.map.flyfloor:
            if pygame.Rect(self.player.x, self.player.y+self.player.height-1, self.player.width, 1).colliderect(i.rect):
                return True, (self.player.x, i.y-self.player.height+1)
        return False, None

    def playerCollideSpike(self):
        """
        check if player collide with spike or not and return the result

        Returns:
            bool: True if player collide with spike, False if not
            tuple: position of player after collision
        """
        for i in self.map.spike:
            if self.player.rect.colliderect(i.rect):
                return True, (30+width*self.spawnstage, -100)
        return False, None

    def playerCollideHedgehog(self):
        """
        check if player collide with hedgehog or not and return the result

        Returns:
            bool: True if player collide with hedgehog, False if not
            tuple: position of player after collision
        """
        for i in self.map.hedgehog:
            if self.player.rect.colliderect(i.rect):
                return True, (30+width*self.spawnstage, -100)
        return False, None
