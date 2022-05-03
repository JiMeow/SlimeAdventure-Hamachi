import pygame
from projectile import Projectile
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, color, name, control=False, **kwargs):
        self.screen = pygame.display.get_surface()

        self.client_data = kwargs["client_data"]
        self.all_sprites_group = kwargs["all_sprites_group"]
        super().__init__(self.all_sprites_group["player"])
        self.init_player_image(pos, color, name)
        self.init_cursor_image()

        self.name = name
        self.control = control
        self.target_pos = list(pos)
        self.speed = player_speed
        self.slow_speed = player_slow_speed
        self.rotate_speed = player_rotation_speed
        self.move_direction = pygame.math.Vector2()
        self.face_direction = pygame.math.Vector2()

    def init_player_image(self, pos, color, name):
        # setup original image
        self.origin_image = pygame.image.load(
            f"FPSmin/assets/{color}.png"
        ).convert()
        self.origin_image = pygame.transform.scale(
            self.origin_image,
            (100, 100)
        )
        self.origin_image.set_colorkey((1, 1, 1))
        # setup text
        text = font.render(str(name), True, "White")
        text_rect = text.get_rect(center=(50, 50))
        pygame.draw.rect(self.origin_image, "Black", text_rect)
        self.origin_image.blit(text, text_rect)
        # setup image and rect
        self.image = self.origin_image
        self.rect = self.image.get_rect(center=pos)

        self.angle = 0

    def init_cursor_image(self):
        self.cursor_image = pygame.surface.Surface(cursor_size).convert()
        self.cursor_image.fill(cursor_color)
        self.cursor_rect = self.cursor_image.get_rect()

    def input(self):
        # self.keyboard()
        self.mouse()

    # def keyboard(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_w]:
    #         self.move_direction.y = -1
    #     elif keys[pygame.K_s]:
    #         self.move_direction.y = 1
    #     else:
    #         self.move_direction.y = 0

    #     if keys[pygame.K_a]:
    #         self.move_direction.x = -1
    #     elif keys[pygame.K_d]:
    #         self.move_direction.x = 1
    #     else:
    #         self.move_direction.x = 0

    def mouse(self):
        mouse = pygame.mouse.get_pos()
        self.face_direction = pygame.math.Vector2(
            mouse[0] - width//2,
            mouse[1] - height//2
        )
        if self.face_direction.magnitude() != 0:
            self.face_direction.normalize_ip()
        if pygame.mouse.get_pressed()[0]:
            if self.face_direction.magnitude() != 0:
                bullet = {
                    "pos": [self.rect.centerx, self.rect.centery],
                    "direction": [self.face_direction.x, self.face_direction.y]
                }
                self.client_data["event"]["bullets"].append(bullet)
                Projectile(
                    self.rect.center,
                    self.face_direction,
                    all_sprites_group=self.all_sprites_group
                )
        if pygame.mouse.get_pressed()[2]:
            self.target_pos = [
                mouse[0] - width//2 + self.rect.centerx,
                mouse[1] - height//2 + self.rect.centery
            ]
            self.client_data["event"]["target_pos"] = self.target_pos[:]

    def move(self, dt):
        self.move_direction = pygame.math.Vector2(
            self.target_pos[0] - self.rect.centerx,
            self.target_pos[1] - self.rect.centery
        )
        if self.move_direction.magnitude() != 0:
            self.move_direction.normalize_ip()
        if pygame.math.Vector2(self.target_pos[0] - self.rect.centerx, self.target_pos[1] - self.rect.centery).magnitude() < (self.move_direction * self.speed * dt).magnitude():
            self.rect.centerx = self.target_pos[0]
            self.rect.centery = self.target_pos[1]
        else:
            self.rect.x += int(self.move_direction.x * self.speed * dt)
            self.rect.y += int(self.move_direction.y * self.speed * dt)

    def draw_cursor(self, screen, offset=pygame.math.Vector2(0, 0)):
        if self.move_direction.magnitude() != 0:
            self.cursor_rect = self.cursor_image.get_rect(
                center=self.target_pos
            )
            # offset.x = int(offset.x * 1.5)
            # offset.y = int(offset.y * 1.5)
            offset_pos = self.cursor_rect.topleft - offset
            screen.blit(self.cursor_image, offset_pos)

    # def rotate(self):
    #     self.image = pygame.transform.rotate(self.origin_image, self.angle)
    #     self.rect = self.image.get_rect(center=self.rect.center)
    #     self.angle += self.rotate_speed

    def update(self, dt):
        if self.control:
            self.input()
        self.move(dt)
        # self.rotate()
