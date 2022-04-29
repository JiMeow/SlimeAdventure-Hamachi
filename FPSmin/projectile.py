import pygame
from glovar import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__(projectile_sprites)
        self.image = pygame.Surface((10, 10))
        self.image.fill("black")
        self.rect = self.image.get_rect(center=(x, y))
        
        self.speed = 20
        self.direction = direction
        self.image = pygame.transform.rotate(self.image, self.direction.angle_to(pygame.math.Vector2(1, 0)))
    
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        
    def life(self):
        if self.rect.x < -10000 or self.rect.x > 10000 or self.rect.y < -10000 or self.rect.y > 10000:
            self.kill()
        
    def update(self):
        self.move()