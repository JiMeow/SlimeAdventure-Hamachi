import pygame

pygame.init()
font = pygame.font.Font(None, 20)

def debug(info,x,y):
    screen = pygame.display.get_surface()
    text = font.render(str(info), True, "White")
    rect = text.get_rect(topleft = (x,y))
    pygame.draw.rect(screen, "Black", rect)
    screen.blit(text, rect)