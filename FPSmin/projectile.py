import pygame
from settings import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, **kwargs):
        super().__init__(kwargs.get("projectile_sprites"))
        self.speed = 20
        # self.rotate_speed = 30
        self.direction = direction
        
        self.max_health = fps * 5
        self.health = fps * 5
        self.original_image = pygame.image.load(f"FPSmin/assets/black.png").convert()
        self.original_image.set_colorkey((1,1,1))
        self.original_image = pygame.transform.scale(self.original_image, (10, 10))
        self.original_image = pygame.transform.rotate(self.original_image, self.direction.angle_to(pygame.math.Vector2(1, 0)))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        
        self.angle = 0
    
    def move(self,dt):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += int(self.direction.x * self.speed * dt)
        self.rect.y += int(self.direction.y * self.speed * dt)
        
    def life(self):
        if self.health <= 0:
            self.kill()
        self.health -= 1
        
    def bounce(self):
        if self.rect.x < 0 or self.rect.x > width:
            self.direction.x *= -1
        if self.rect.y < 0 or self.rect.y > height:
            self.direction.y *= -1
        
    # def rotate(self):
    #     self.image = pygame.transform.rotate(self.original_image, self.angle)
    #     self.rect = self.image.get_rect(center=self.rect.center)
    #     self.angle += self.max_health - self.health
        
    def update(self,dt):
        self.move(dt)
        # self.bounce()
        # self.rotate()
        self.life()