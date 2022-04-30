import pygame
from glovar import *
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__(projectile_sprites)
        self.speed = 20
        self.direction = direction
        
        self.health = 5 * 60
        self.image = pygame.Surface((10, 10))
        self.image.fill("black")
        self.image = pygame.transform.rotate(self.image, self.direction.angle_to(pygame.math.Vector2(0, 1)))
        self.rect = self.image.get_rect(center=(x, y))
    
    def move(self,dt):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += (self.direction.x * self.speed * dt * fps)//1000
        self.rect.y += (self.direction.y * self.speed * dt * fps)//1000
        
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