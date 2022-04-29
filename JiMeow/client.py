import pygame
from threading import *
from network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

pygame.init()
font = pygame.font.Font(None, 20)


def debug(info, x, y):
    screen = pygame.display.get_surface()
    text = font.render(str(info), True, "White")
    rect = text.get_rect(topleft=(x, y))
    pygame.draw.rect(screen, "Black", rect)
    screen.blit(text, rect)


def redrawWindow(win, p, allp):
    win.fill((255, 255, 255))
    for i in allp:
        if i.id != p.id:
            i.draw(win)
            i.drawname(win)
        else:
            p.update()
            p.draw(win)
            p.drawname(win)


def getDataP(network, p, tempallp=[]):
    while(len(tempallp) != 0):
        tempallp.pop(0)
    tempallp += network.send(p)
    return tempallp


def main():
    run = True
    n = Network()
    p = n.getP()
    username = input("Username: ")
    p.name = username
    clock = pygame.time.Clock()
    frame = 0
    allp = getDataP(n, p)
    tempallp = list(allp)
    thread = Thread(target=getDataP, args=(n, p, tempallp))

    while run:

        clock.tick(60)

        if not thread.is_alive():
            allp = list(tempallp)
            thread = Thread(target=getDataP, args=(n, p, tempallp))
            thread.start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()

        if not thread.is_alive():
            allp = list(tempallp)

        redrawWindow(win, p, allp)
        debug(f"{clock.get_fps():.2f}", 0, 0)
        pygame.display.update()

        frame += 1


main()
