import pygame
from threading import *
from network import Network
from setting import *
from map import Map
import time
import os


username = input("Username: ")
while len(username) > 6:
    os.system('cls')
    print("length of username must lest than 6")
    username = input("Username: ")


win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

screen = Map(win, "JiMeow/photo/forest.png")
font = pygame.font.Font(None, 20)


def debug(info, x, y):
    screen = pygame.display.get_surface()
    text = font.render(str(info), True, "White")
    rect = text.get_rect(topleft=(x, y))
    pygame.draw.rect(screen, "Black", rect)
    screen.blit(text, rect)


def redrawWindow(win, p, allp, dt):
    screen.draw()
    debug(f"{clock.get_fps():.2f}", 0, 0)
    # debug(f"{allp[0].x},{allp[0].y}", 0, 20)
    for i in allp:
        if i.id != p.id:
            i.draw(win)
            i.drawname(win)
    for i in allp:
        if i.id == p.id:
            p.update(dt)
            p.draw(win)
            p.drawname(win)


def getDataP(network, p, tempallp=[]):
    while(len(tempallp) != 0):
        tempallp.pop(0)
    tempallp += network.send(p)
    return tempallp


def predictMove(p, allp, dt):
    for i in allp:
        if i.id != p.id:
            i.update(dt)


def main():
    run = True
    n = Network()
    p = n.getP()
    p.name = username
    frame = 0
    allp = getDataP(n, p)
    tempallp = list(allp)
    thread = Thread(target=getDataP, args=(n, p, tempallp))
    beforetime = time.time()

    while run:
        isPlayerJump = False
        dt = time.time() - beforetime
        beforetime = time.time()
        if not thread.is_alive():
            allp = list(tempallp)
            thread = Thread(target=getDataP, args=(n, p, tempallp))
            thread.start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isPlayerJump = True

        p.move()
        p.jump(screen.g, isPlayerJump)
        p.update(dt)

        if not thread.is_alive():
            allp = list(tempallp)
        else:
            predictMove(p, allp, dt)

        redrawWindow(win, p, allp, dt)
        pygame.display.update()

        frame += 1


main()
