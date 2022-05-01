import pygame
from glovar import *
from projectile import Projectile
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, name, control=False):
        super().__init__(player_sprites)
        self.screen = pygame.display.get_surface()
        self.init_player_image(color, name, x, y)
        self.init_cursor_image()
        self.name = name
        self.speed = 3
        # self.rotate_speed = 30
        self.control = control
        self.target_pos = (x, y)
        self.move_direction = pygame.math.Vector2()
        self.face_direction = pygame.math.Vector2()
        
    def init_player_image(self, color, name, x, y):
        # setup original image
        self.original_image = pygame.image.load(f"FPSmin/assets/{color}.png").convert()
        self.original_image = pygame.transform.scale(self.original_image, (100, 100))
        self.original_image.set_colorkey((0,0,0))
        # setup text
        text = font.render(str(name), True, "White")
        text_rect = text.get_rect(center = (50, 50))
        pygame.draw.rect(self.original_image, "Black", text_rect)
        self.original_image.blit(text,text_rect)
        # setup image and rect
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        
        self.angle = 0
        
    def init_cursor_image(self):
        self.cursor_image = pygame.surface.Surface((8, 8)).convert()
        self.cursor_image.fill((255, 255, 255))
        self.cursor_rect = self.cursor_image.get_rect()
        
        
    def input(self):
        # self.keyboard()
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
        if self.face_direction.magnitude() != 0:
            self.face_direction = self.face_direction.normalize()
        if pygame.mouse.get_pressed()[0]:
            if self.face_direction.magnitude() != 0:
                bullet = {"pos": [self.rect.centerx, self.rect.centery], "direction": [self.face_direction.x, self.face_direction.y]}
                client_data["event"]["bullets"].append(bullet)
                Projectile(self.rect.centerx, self.rect.centery, self.face_direction)
        if pygame.mouse.get_pressed()[2]:
            self.target_pos = mouse
        self.move_direction = pygame.math.Vector2(self.target_pos[0] - self.rect.centerx, self.target_pos[1] - self.rect.centery)
        
    def interpolation(self):
        pass
        
    def exterpolation(self):
        pass
        
    def move(self,dt):
        if self.move_direction.magnitude() != 0:
            self.move_direction.normalize_ip()
        if pygame.math.Vector2(self.target_pos[0] - self.rect.centerx, self.target_pos[1] - self.rect.centery).magnitude() < (self.move_direction * self.speed * dt).magnitude():
            self.rect.centerx = self.target_pos[0]
            self.rect.centery = self.target_pos[1]
        else:
            self.rect.x += int(self.move_direction.x * self.speed * dt)
            self.rect.y += int(self.move_direction.y * self.speed * dt)

    def draw_cursor(self):
        if self.move_direction.magnitude() != 0:
            self.cursor_rect = self.cursor_image.get_rect(center = self.target_pos)
            self.screen.blit(self.cursor_image, self.cursor_rect)
            
    # def rotate(self):
    #     self.image = pygame.transform.rotate(self.original_image, self.angle)
    #     self.rect = self.image.get_rect(center=self.rect.center)
    #     self.angle += self.rotate_speed
    
    def update(self,dt):
        if self.control:
            self.input()
            self.move(dt)
            self.draw_cursor()
        # self.rotate()