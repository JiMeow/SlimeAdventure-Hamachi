import pygame
import os

pygame.init()
font_size = 20
font = pygame.font.Font(None, font_size)


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


def create_surface(size, color=None, colorkey=(0, 0, 0)):
    surface = pygame.Surface(size).convert()
    surface.set_colorkey(colorkey)
    if color:
        surface.fill(color)
    return surface


def debug(info, debug_count):
    screen = pygame.display.get_surface()
    text = font.render(str(info), True, "White")
    rect = text.get_rect(topleft=(0, debug_count[0] * (font_size//2+2)))
    pygame.draw.rect(screen, "Black", rect)
    screen.blit(text, rect)
    debug_count[0] += 1


lt = 0
t = 0
dt = 0


def get_dt(fps):
    global lt, t, dt
    t = pygame.time.get_ticks()
    dt = (t - lt) * fps / 1000
    lt = t
    return dt
