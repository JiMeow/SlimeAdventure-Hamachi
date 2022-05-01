import pygame
from glovar import *
from projectile import Projectile
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, name, control=False):
        super().__init__(player_sprites)
        self.init_image(color, name, x, y)

        self.name = name
        self.speed = 10
        # self.rotate_speed = 30
        self.control = control
        self.move_direction = pygame.math.Vector2()
        self.face_direction = pygame.math.Vector2()
        
        
        
    def init_image(self, color, name, x, y):
        # setup original image
        self.original_image = pygame.image.load(f"FPSmin/assets/{color}.png").convert()
        self.original_image = pygame.transform.scale(self.original_image, (100, 100))
        self.original_image.set_colorkey((0,0,0))
        # setup text
        text = font.render(str(name), True, "White")
        text_rect = text.get_rect(center = (50, 50))
        pygame.draw.rect(self.original_image, "Black", text_rect)
        self.original_image.blit(text,text_rect)
        
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        
        self.angle = 0
        
    def input(self):
        self.keyboard()
        self.mouse()
    def keyboard(self):
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
                bullet = {"pos": [self.rect.centerx, self.rect.centery], "direction": [self.face_direction.x, self.face_direction.y]}
                client_data["event"]["bullets"].append(bullet)
                Projectile(self.rect.centerx, self.rect.centery, self.face_direction)
        
    def interpolation(self):
        pass
        
    def exterpolation(self):
        pass
        
    def move(self,dt):
        if self.move_direction.magnitude() != 0:
            self.move_direction = self.move_direction.normalize()
        
        self.rect.x += int(self.move_direction.x * self.speed * dt)
        self.rect.y += int(self.move_direction.y * self.speed * dt)

    
    # def rotate(self):
    #     self.image = pygame.transform.rotate(self.original_image, self.angle)
    #     self.rect = self.image.get_rect(center=self.rect.center)
    #     self.angle += self.rotate_speed
    
    def update(self,dt):
        if self.control:
            self.input()
            self.move(dt)
        # self.rotate()