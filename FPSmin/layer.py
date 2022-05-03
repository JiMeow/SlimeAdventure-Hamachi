import pygame
from settings import *
from cameragroup import CameraGroup


class Layer:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        # sprite groups
        self.all_sprites_groups = []
        self.camera = CameraGroup(self.all_sprites_groups)

        self.lt = 0
        self.t = 0
        self.dt = 0

    def set_sprite_groups(self, *sprite_groups):
        self.all_sprites_groups += list(sprite_groups)

    def render(self, player):
        self.set_dt()
        self.update()

        self.screen.fill(background_color)
        self.camera.camera_render(player)
        # self.default_render(player)

    def default_render(self, player):
        self.screen.blit(self.background_image, self.background_rect)
        player.draw_cursor(self.screen)
        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect)

    def set_dt(self):
        self.t = pygame.time.get_ticks()
        self.dt = (self.t - self.lt) * fps / 1000
        self.lt = self.t

    def update(self):
        for sprites_group in self.all_sprites_groups:
            sprites_group.update(self.dt)
