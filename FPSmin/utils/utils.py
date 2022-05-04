import pygame
import os


def draw_text_to_surface(surface, font, text, text_color, bg_color, pos):
    text = font.render(str(text), True, text_color)
    text_rect = text.get_rect(center=pos)
    pygame.draw.rect(surface, bg_color, text_rect)
    surface.blit(text, text_rect)


def load_img(path, colorkey=(0, 0, 0), size=None):
    img = pygame.image.load(path).convert()
    if size:
        img = pygame.transform.scale(img, size)
    img.set_colorkey(colorkey)
    return img


def load_ani(path, colorkey=(0, 0, 0), size=None):
    ani = []
    for filename in os.listdir(path):
        img_path = os.path.join(path, filename)
        ani.append(load_img(img_path, colorkey, size))
    return ani
