import pygame
from src.setting import *


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
        if self.player.y >= floor-self.player.height:
            return True, (self.player.x, floor-self.player.height)
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
            for j in i.hitbox:
                if self.player.rect.colliderect(j):
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

    def playerCollideJellyFish(self):
        """
        check if player collide with jellyfish or not and return the result

        Returns:
            bool: True if player collide with jellyfish, False if not
            tuple: position of player after collision
        """
        for i in self.map.jellyfish:
            if self.player.rect.colliderect(i.rect):
                return True, (30+width*self.spawnstage, -100)
        return False, None

    def playerCollideJumpBoost(self):
        """
        check if player collide with uni or not and return the result

        Returns:
            bool: True if player collide with uni, False if not
            tuple: position of player after collision
        """
        for i in self.map.jumpboost:
            if self.player.rect.colliderect(i.rect):
                i.used()
                return True, None
        return False, None

    def playerCollideWall(self):
        """
        check if player collide with wall or not and return the result

        Returns:
            bool: True if player collide with wall, False if not
            tuple: position of player after collision
        """
        playerhitboxleft = [pygame.Rect(
            self.player.x, self.player.y+7+4*(i+1), 1, 1) for i in range(5)]
        playerhitboxright = [pygame.Rect(
            self.player.x+self.player.width-1, self.player.y+7+4*(i+1), 1, 1) for i in range(5)]
        playerhitboxup = [pygame.Rect(
            self.player.x+10+6*(i+1), self.player.y, 1, 1) for i in range(5)]
        playerhitboxdown = [pygame.Rect(
            self.player.x+10+6*(i+1), self.player.y+self.player.height-1, 1, 1) for i in range(5)]
        direction = {
            "up": 0, "down": 0, "left": 0, "right": 0
        }
        mask = False
        posdown = None
        for i in self.map.wall:
            for j in playerhitboxup:
                if j.colliderect(i.rect):
                    direction["up"] += 1
                    mask = True
            for j in playerhitboxleft:
                if j.colliderect(i.rect):
                    direction["left"] += 1
                    mask = True
            for j in playerhitboxright:
                if j.colliderect(i.rect):
                    direction["right"] += 1
                    mask = True
            for j in playerhitboxdown:
                if j.colliderect(i.rect):
                    posdown = i.rect.y
                    direction["down"] += 1
                    mask = True
        return mask, sorted(list(direction.items()), key=lambda x: x[1], reverse=True)[0], posdown
