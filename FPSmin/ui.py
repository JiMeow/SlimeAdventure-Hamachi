import pygame
from settings import *
import math

"""
projectile types have 8 types
1.water(q)
2.heal(w)
3.shield(e)
4.ice(r)
5.thunder(a)
6.death(s)
7.stone(d)
8.fire(f)
"""


class UIElement(pygame.sprite.Sprite):
    def __init__(self, group, pos, element, key):
        super().__init__(group)
        self.radius = UI_element_image_size[0]//2
        self.img1 = create_surface(
            UI_element_image_size, (0, 0, 0), (0, 0, 0)
        )
        pygame.draw.circle(
            self.img1, (1, 1, 1),
            (UI_element_image_size[0]//2, UI_element_image_size[1]//2),
            UI_element_image_size[0]//2
        )

        self.img2 = create_surface(
            UI_element_image_size, (0, 0, 0), (0, 0, 0)
        )
        pygame.draw.circle(
            self.img2, (255, 255, 255),
            (UI_element_image_size[0]//2, UI_element_image_size[1]//2),
            UI_element_image_size[0]//2
        )

        self.image = self.img1
        self.rect = self.image.get_rect(topleft=pos)
        self.key = key
        self.hovered = False
        self.pressed = False
        if element == "water":
            pass
        if element == "heal":
            pass
        if element == "shield":
            pass
        if element == "ice":
            pass
        if element == "thunder":
            pass
        if element == "death":
            pass
        if element == "stone":
            pass
        if element == "fire":
            pass

    def collide_mouse(self):
        x1, y1 = pygame.mouse.get_pos()
        x2, y2 = self.rect.center
        distance = math.hypot(x1 - x2, y1 - y2)
        if distance <= self.radius:
            return True
        return False

    def hover(self):
        if self.collide_mouse():
            self.hovered = True

    def press(self):
        keys = pygame.key.get_pressed()
        if keys[self.key]:
            self.pressed = True

    def animate(self):
        if self.hovered or self.pressed:
            self.image = self.img2
        else:
            self.image = self.img1
        self.hovered = False
        self.pressed = False

    def update(self):
        self.hover()
        self.press()
        self.animate()


class UIGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.create_element()

    def create_element(self):
        order = UI_element_order
        keys = UI_element_keys
        k = 0
        stepx = UI_element_image_size[0] + 1
        stepy = UI_element_image_size[1] - 1
        for i in range(2):
            for j in range(4):
                x = width//2 - (10 - i) * stepx//2 + j * stepx
                y = height - 2 * stepy + i * stepy
                UIElement(self, (x, y), order[k], keys[k])
                print(x, y, order[k])
                k += 1

    def draw(self):
        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect)

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()
