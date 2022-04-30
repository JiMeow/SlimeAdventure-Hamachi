import pygame

pygame.init()
font_size = 20
font = pygame.font.Font(None, font_size)

def debug(info, debug_count):
    screen = pygame.display.get_surface()
    text = font.render(str(info), True, "White")
    rect = text.get_rect(topleft = (0, debug_count[0] * (font_size//2+2)))
    pygame.draw.rect(screen, "Black", rect)
    screen.blit(text, rect)
    debug_count[0] += 1