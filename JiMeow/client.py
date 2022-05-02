import pygame
from threading import *
from setting import *
from collision import Collision
from layout import Layout
from network import Network
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
    layout.setCollision(collision)
    layout.setScreen(screen)
    layout.setPlayer(p)
    layout.setAllPlayer(allp)
    layout.setDt(dt)
    layout.drawPlayerFrame()
    debug(f'{clock.get_fps():.2f}', 0, 0)


def getDataP(network, p, tempallp=[], tempstatus={0: False, 1: False, 2: False, 3: False}):
    while(len(tempallp) != 0):
        tempallp.pop(0)
    data = network.send(p)
    tempallp += data["players"]
    for i in range(4):
        tempstatus[i] = data["status"][i]
    return tempallp, tempstatus


def exterpolation(p, allp, dt, collision, status):
    for i in allp:
        if i.id != p.id and status[i.id-1]:
            i.jump(False, screen.gravity, dt)
            collision.setPlayer(i)
            i.update(dt, collision)


def setNewCollision(p, allp, collision):
    collision.setPlayer(p)
    collision.setAllPlayer(allp)
    collision.setMap(screen)


def test(p, stage):
    p.x += width*stage


def main():
    run = True
    n = Network()
    p = n.getP()
    # test(p, 1)
    p.name = username
    frame = 0

    allp, status = getDataP(n, p)
    tempallp = list(allp)
    tempstatus = dict(status)

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
            status = dict(tempstatus)
            thread = Thread(target=getDataP, args=(n, p, tempallp, tempstatus))
            thread.start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                n.disconnect()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                    isPlayerJump = True

        p.move()
        p.jump(isPlayerJump, screen.gravity, dt)
        setNewCollision(p, allp, collision)
        p.update(dt, collision)

        if not thread.is_alive():
            allp = list(tempallp)
            status = dict(tempstatus)
        else:
            exterpolation(p, allp, dt, collision, status)

        setNewCollision(p, allp, collision)
        redrawWindow(layout, p, allp, dt, collision)
        frame += 1


main()
