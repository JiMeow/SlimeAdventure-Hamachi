import pygame
from glovar import *
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__(projectile_sprites)
        self.speed = 20
        self.direction = direction
        
        self.health = fps * 5
        self.image = pygame.image.load(f"FPSmin/assets/black.png").convert()
        self.image.set_colorkey((1,1,1))
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.image = pygame.transform.rotate(self.image, self.direction.angle_to(pygame.math.Vector2(1, 0)))
        self.rect = self.image.get_rect(center=(x, y))
    
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
        
    def update(self,dt):
        self.move(dt)
        self.bounce()
        self.life()