import pygame
from setting import *


class Player():
    def __init__(self, id, x, y, width, height, color, name):
        """
        set player infomation

        Args:
            id (int): id of player
            x (int): x position of player
            y (int): y position of player
            width (int): width of player
            height (int): height of player
            color (tuple): color of player
            name (str): name of player
        """
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 2
        self.speed = [0, 0]
        self.name = name
        self.jumpcount = 0

        self.on = {"Ground": False, "Slab": False}

        # use for drop to floor fromm slab
        self.dropTo = 0

    def draw(self, win, stage=0):
        """
        draw player img at stage by rect

        Args:
            win (pygame.display): pygame window
            stage (int): stage of game. Defaults to 0.
        """
        pygame.draw.rect(win, self.color, pygame.Rect(
            self.rect.x-width*stage, self.rect.y, self.rect.width, self.rect.height))

    def drawname(self, win, stage=0):
        """
        draw player name at stage by rect

        Args:
            win (pygame.display): pygame window
            stage (int): stage of game. Defaults to 0.
        """
        font = pygame.font.Font(None, 20)
        text = font.render(str(self.name), True, "White")
        rect = text.get_rect()
        rect.center = self.rect.center
        rect.x -= width*stage
        win.blit(text, rect)

    def move(self):
        """
        control player move by keyboard then change speed of player
        if player on slab and press key 'down' or 's' then drop from slab 
        can not move is player not in frame of screen
        """
        keys = pygame.key.get_pressed()
        cnt = 0
        if self.y >= -self.height:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.speed[0] = -1
            else:
                cnt += 1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.speed[0] = 1
            else:
                cnt += 1
            if cnt == 2:
                self.speed[0] = 0
            self.speed[0] = self.speed[0] * self.vel
        else:
            self.speed[0] = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.on["Slab"]:
                self.dropTo = self.y+15
                self.on["Slab"] = False

    def jump(self, isJump, gravity, dt):
        """
        if isJump is True then jump by set player jump 
        by change y_axis speed of player and change jumpcount
        update on status then let player fall by gravity

        Args:
            isJump (bool): player is jump or not
            gravity (float): gravity of map
            dt (float): delta time check for lag
        """
        if isJump:
            if self.jumpcount < 2:
                self.jumpcount += 1
                self.speed[1] = -6
                self.on["Ground"] = False
                self.on["Slab"] = False
        self.fall(gravity, dt)

    def fall(self, gravity, dt):
        """
        generate player fall by change player speed 
        that depend on gravity and delta time

        Args:
            gravity (float): gravity of map
            dt (float): delta time check for lag
        """
        if not self.on["Ground"] and not self.on["Slab"]:
            self.speed[1] = min(self.speed[1] + gravity*60*dt, 15)

    def update(self, dt=1/60, collision=None):
        """
        update player position by speed and delta time then 
        set player (x,y) position to collision information
        then check collision with all obstacle in map 
        and update information of player

        Args:
            dt (float, float): delta time check for lag. Defaults to 1/60.
            collision (Collision, Nonce): collision information for check collision. Defaults to None.
        """
        self.x += self.speed[0] * 60 * dt
        self.y += self.speed[1] * 60 * dt
        collision.setPlayerXY(self.x, self.y)

        # on slab
        mask, pos = collision.playerCollideFloor()
        if mask:
            self.speed[1] = 0
            self.jumpcount = 0
            self.y = pos[1]
            self.on["Ground"] = True
        else:
            self.on["Ground"] = False

        # drop to floor from slab
        if self.y > self.dropTo:
            self.dropTo = 0
            mask, pos = collision.playerCollideFlyingFloor()
            if mask:
                if self.speed[1] >= 0:
                    self.speed[1] = 0
                    self.jumpcount = 0
                    self.y = pos[1]
                    self.on["Slab"] = True
                else:
                    self.on["Slab"] = False
            else:
                self.on["Slab"] = False

        # hit spike
        mask, pos = collision.playerCollideSpike()
        if mask:
            self.x, self.y = pos
            self.jump(True, 6, dt)
            self.jumpcount = 0
        # hit hedgehog
        mask, pos = collision.playerCollideHedgehog()
        if mask:
            self.x, self.y = pos
            self.jump(True, 6, dt)
            self.jumpcount = 0

        # hit jelly fish
        mask, pos = collision.playerCollideJellyFish()
        if mask:
            self.x, self.y = pos
            self.jump(True, 6, dt)
            self.jumpcount = 0

        # hit jumpboost
        mask, pos = collision.playerCollideJumpBoost()
        if mask:
            self.jumpcount = 0

        # no negative stage
        if self.x < 0:
            self.x = 0
        # print(self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
