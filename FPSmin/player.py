import pygame
from projectile import Projectile
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, color, name, control=False, **kwargs):
        self.screen = pygame.display.get_surface()

        self.client_sending_data = kwargs.get("client_sending_data")
        self.all_sprites_group = kwargs["all_sprites_group"]
        super().__init__(self.all_sprites_group["player"])
        self.init_player_image(pos, color, name)
        self.init_cursor_image()

        self.name = name
        self.control = control
        self.target_pos = list(pos)
        self.normal_speed = player_normal_speed
        self.slow_speed = player_slow_speed
        self.speed = self.normal_speed
        self.rotate_speed = player_rotation_speed
        self.move_direction = pygame.math.Vector2()
        self.face_direction = pygame.math.Vector2()
        self.is_shoot = False

    def init_player_image(self, pos, color, name):
        # setup original image
        if color == "red":
            self.origin_image = player_image_red
        elif color == "green":
            self.origin_image = player_image_green
        self.origin_image = pygame.transform.scale(
            self.origin_image,
            player_image_size
        )
        # setup text
        draw_text_to_surface(
            surface=self.origin_image,
            font=font,
            text=name,
            text_color="white",
            bg_color="black",
            pos=[
                player_image_size[0]//2,
                player_image_size[1]//2
            ]
        )
        # setup image and rect
        self.image = self.origin_image
        self.rect = self.image.get_rect(center=pos)

        self.angle = 0

    def init_cursor_image(self):
        self.cursor_image = pygame.surface.Surface(cursor_size).convert()
        self.cursor_image.fill(cursor_color)
        self.cursor_rect = self.cursor_image.get_rect()

    def draw_cursor(self, screen, offset=pygame.math.Vector2(0, 0)):
        if self.move_direction.magnitude() != 0:
            self.cursor_rect = self.cursor_image.get_rect(
                center=self.target_pos
            )
            # offset.x = int(offset.x * 1.5)
            # offset.y = int(offset.y * 1.5)
            offset_pos = self.cursor_rect.topleft - offset
            screen.blit(self.cursor_image, offset_pos)

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

    def set_face_direction(self):
        mouse = pygame.mouse.get_pos()
        self.face_direction = pygame.math.Vector2(
            mouse[0] - width//2,
            mouse[1] - height//2
        )

    def walk(self):
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[2]:
            self.target_pos = [
                mouse[0] - width//2 + self.rect.centerx,
                mouse[1] - height//2 + self.rect.centery
            ]
            self.client_sending_data["event"]["target_pos"] = self.target_pos

    def shoot(self):
        if self.is_shoot:
            self.is_shoot = False
        if pygame.mouse.get_pressed()[0]:
            if self.face_direction.magnitude() != 0:
                self.is_shoot = True
                self.face_direction.normalize_ip()
                bullet = {
                    "pos": [self.rect.centerx, self.rect.centery],
                    "direction": [self.face_direction.x, self.face_direction.y]
                }
                self.client_sending_data["event"]["bullets"].append(bullet)
                Projectile(
                    self.rect.center,
                    self.face_direction,
                    all_sprites_group=self.all_sprites_group
                )

    def move(self, dt):
        self.move_direction = pygame.math.Vector2(
            self.target_pos[0] - self.rect.centerx,
            self.target_pos[1] - self.rect.centery
        )
        if self.move_direction.magnitude() != 0:
            if self.move_direction.magnitude() < (self.move_direction.normalize() * self.speed * dt).magnitude():
                self.rect.centerx = self.target_pos[0]
                self.rect.centery = self.target_pos[1]
            else:
                self.move_direction.normalize_ip()
                self.rect.x += int(self.move_direction.x *
                                   self.speed * dt)
                self.rect.y += int(self.move_direction.y *
                                   self.speed * dt)

    def set_speed(self):
        if self.is_shoot:
            self.speed = self.slow_speed
        else:
            if self.speed == self.slow_speed:
                self.speed = self.normal_speed
    # def rotate(self):
    #     self.image = pygame.transform.rotate(self.origin_image, self.angle)
    #     self.rect = self.image.get_rect(center=self.rect.center)
    #     self.angle += self.rotate_speed

    def update(self, dt):
        if self.control:
            self.set_face_direction()
            self.walk()
            self.shoot()
            # self.keyboard()
        self.set_speed()
        self.move(dt)
        # self.rotate()
