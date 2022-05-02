import pygame
from setting import *


class Player():
    def __init__(self, id, x, y, width, height, color, name):
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
        pygame.draw.rect(win, self.color, pygame.Rect(
            self.rect.x-width*stage, self.rect.y, self.rect.width, self.rect.height))

    def drawname(self, win, stage=0):
        font = pygame.font.Font(None, 20)
        text = font.render(str(self.name), True, "White")
        rect = text.get_rect()
        rect.center = self.rect.center
        rect.x -= width*stage
        win.blit(text, rect)

    def move(self):
        keys = pygame.key.get_pressed()
        cnt = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed[0] = -1
        else:
            cnt += 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed[0] = 1
        else:
            cnt += 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.on["Slab"]:
                self.dropTo = self.y+15
                self.on["Slab"] = False
        if cnt == 2:
            self.speed[0] = 0
        self.speed[0] = self.speed[0] * self.vel

    def jump(self, isJump, gravity, dt):
        if isJump:
            if self.jumpcount < 2:
                self.jumpcount += 1
                self.speed[1] = -6
                self.on["Ground"] = False
                self.on["Slab"] = False
        self.fall(gravity, dt)

    def fall(self, gravity, dt):
        if not self.on["Ground"] and not self.on["Slab"]:
            self.speed[1] = min(self.speed[1] + gravity*60*dt, 15)

    def update(self, dt=1/60, collision=None):
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

        # no negative stage
        if self.x < 0:
            self.x = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
