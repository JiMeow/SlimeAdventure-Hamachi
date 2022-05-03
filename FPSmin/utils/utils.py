import pygame


def load_img(path):
    img = pygame.image.load(path).convert()
    img.set_colorkey((0, 0, 0))
    return img
