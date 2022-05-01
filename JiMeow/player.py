import pygame
from setting import *
from collision import Collision


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

    def draw(self, win, stage=0):
        pygame.draw.rect(win, self.color, pygame.Rect(
            self.rect.x-width*stage, self.rect.y, self.rect.width, self.rect.height))
        # pygame.draw.rect(win, self.color, self.rect)

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
        if keys[pygame.K_LEFT]:
            self.speed[0] = -1
        else:
            cnt += 1
        if keys[pygame.K_RIGHT]:
            self.speed[0] = 1
        else:
            cnt += 1
        if cnt == 2:
            self.speed[0] = 0
        self.speed[0] = self.speed[0] * self.vel

    def jump(self, isJump, gravity, dt):
        # print(dt*60)
        if isJump:
            if self.jumpcount < 2:
                self.jumpcount += 1
                self.speed[1] = -6
        self.speed[1] = min(self.speed[1] + gravity*60*dt, 15)

    def update(self, dt=1/60, collision=None):
        self.x += self.speed[0] * 60 * dt
        self.y += self.speed[1] * 60 * dt
        if collision.playerCollideFloor():
            self.speed[1] = 0
            self.jumpcount = 0
            self.y = floor
        if collision.playerCollideFlyingFloor():
            self.speed[1] = 0
            self.jumpcount = 0
            self.y = 540
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
