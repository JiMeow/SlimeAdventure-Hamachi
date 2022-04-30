import pygame
from glovar import *
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, control=False):
        super().__init__(player_sprites)
        self.image = pygame.Surface((100, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        
        self.speed = 10
        self.control = control
        self.move_direction = pygame.math.Vector2()
        self.face_direction = pygame.math.Vector2(0, 1)
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_direction.y = -1
        elif keys[pygame.K_s]:
            self.move_direction.y = 1
        else:
            self.move_direction.y = 0

        if keys[pygame.K_a]:
            self.move_direction.x = -1
        elif keys[pygame.K_d]:
            self.move_direction.x = 1
        else:
            self.move_direction.x = 0
    
    def mouse(self):
        mouse = pygame.mouse.get_pos()
        self.face_direction = pygame.math.Vector2(mouse[0] - self.rect.centerx, mouse[1] - self.rect.centery)
        try:
            self.face_direction = self.face_direction.normalize()
        except:
            pass
        if pygame.mouse.get_pressed()[0]:
            if self.face_direction.magnitude() != 0:
                client_data["event"]["pos"] = [self.rect.centerx, self.rect.centery]
                client_data["event"]["direction"] = [self.face_direction.x, self.face_direction.y]
                Projectile(self.rect.centerx, self.rect.centery, self.face_direction)
        
    def move(self,dt):
        if self.move_direction.magnitude() != 0:
            self.move_direction = self.move_direction.normalize()
        
        self.rect.x += (self.move_direction.x * self.speed * dt * 60)//1000
        self.rect.y += (self.move_direction.y * self.speed * dt * 60)//1000
        
    def update(self,dt):
        if self.control:
            self.input()
            self.mouse()
            self.move(dt)