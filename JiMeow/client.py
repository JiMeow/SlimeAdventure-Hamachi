import pygame
from threading import *
from collision import Collision
from layout import Layout
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


def debug(info, x, y):
    font = pygame.font.Font(None, 20)
    screen = pygame.display.get_surface()
    text = font.render(str(info), True, "White")
    rect = text.get_rect(topleft=(x, y))
    pygame.draw.rect(screen, "Black", rect)
    screen.blit(text, rect)


def redrawWindow(layout, p, allp, dt, collision):
    layout.addCollision(collision)
    layout.addScreen(screen)
    layout.addPlayer(p)
    layout.addAllPlayer(allp)
    layout.addDt(dt)
    layout.drawPlayerFrame()
    debug(f'{clock.get_fps():.2f}', 0, 0)


def getDataP(network, p, tempallp=[]):
    while(len(tempallp) != 0):
        tempallp.pop(0)
    tempallp += network.send(p)
    return tempallp


def exterpolation(p, allp, dt, collision):
    for i in allp:
        if i.id != p.id:
            i.jump(False, screen.gravity, dt)
            collision.addPlayer(i)
            i.update(dt, collision)


def setNewCollision(p, allp, collision):
    collision.addPlayer(p)
    collision.addAllPlayer(allp)
    collision.addMap(screen)


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
    layout = Layout(win)
    collision = Collision(p, allp, screen)

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
                n.disconnect()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isPlayerJump = True

        p.move()
        p.jump(isPlayerJump, screen.gravity, dt)
        setNewCollision(p, allp, collision)
        p.update(dt, collision)

        if not thread.is_alive():
            allp = list(tempallp)
        else:
            exterpolation(p, allp, dt, collision)

        setNewCollision(p, allp, collision)
        redrawWindow(layout, p, allp, dt, collision)
        frame += 1


main()
