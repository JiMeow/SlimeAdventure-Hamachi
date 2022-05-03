import pygame


def load_img(path, colorkey=(0, 0, 0)):
    img = pygame.image.load(path).convert()
    img.set_colorkey(colorkey)
    return img


def draw_text_to_surface(surface, font, text, text_color, bg_color, pos):
    text = font.render(str(text), True, text_color)
    text_rect = text.get_rect(center=pos)
    pygame.draw.rect(surface, bg_color, text_rect)
    surface.blit(text, text_rect)
