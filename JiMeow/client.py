import pygame
from threading import *
from setting import *
from collision import Collision
from layout import Layout
from network import Network
from map import Map
from ui import Login
import time
import os


def debug(info, x, y):
    font = pygame.font.Font(None, 20)
    screen = pygame.display.get_surface()
    text = font.render(str(info), True, "White")
    rect = text.get_rect(topleft=(x, y))
    pygame.draw.rect(screen, "Black", rect)
    screen.blit(text, rect)


def redrawWindow(layout, p, allp, dt, collision, map):
    layout.setCollision(collision)
    layout.setScreen(map)
    layout.setPlayer(p)
    layout.setAllPlayer(allp)
    layout.setDt(dt)
    layout.drawPlayerFrame()
    # debug(f'{clock.get_fps():.2f}', 0, 0)


def getDataP(network, p, tempallp=[], tempstatus={0: False, 1: False, 2: False, 3: False}):
    while(len(tempallp) != 0):
        tempallp.pop(0)
    data = network.send(p)
    tempallp += data["players"]
    for i in range(4):
        tempstatus[i] = data["status"][i]
    return tempallp, tempstatus


def exterpolation(p, allp, dt, collision, status, map):
    for i in allp:
        if i.id != p.id and status[i.id-1]:
            i.jump(False, map.gravity, dt)
            collision.setPlayer(i)
            i.update(dt, collision)


def setNewCollision(p, allp, collision, map):
    collision.setPlayer(p)
    collision.setAllPlayer(allp)
    collision.setMap(map)


def test(p, stage):
    p.x += width*stage


def game(username):
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Client")
    pygame.init()
    clock = pygame.time.Clock()

    run = True
    n = Network()
    p = n.getP()
    # test(p, 1)
    p.name = username
    frame = 0
    map = Map(win, "JiMeow/photo/forest.png")

    allp, status = getDataP(n, p)
    tempallp = list(allp)
    tempstatus = dict(status)

    thread = Thread(target=getDataP, args=(n, p, tempallp))
    beforetime = time.time()
    layout = Layout(win)
    collision = Collision(p, allp, map)

    while run:
        clock.tick(60)
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
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                    isPlayerJump = True
        if not run:
            break
        p.move()
        p.jump(isPlayerJump, map.gravity, dt)
        setNewCollision(p, allp, collision, map)
        p.update(dt, collision)

        if not thread.is_alive():
            allp = list(tempallp)
            status = dict(tempstatus)
        else:
            exterpolation(p, allp, dt, collision, status, map)

        setNewCollision(p, allp, collision, map)
        redrawWindow(layout, p, allp, dt, collision, map)
        frame += 1


def main():
    username = []
    ui = Login(username)
    while(1):
        ui.show()
        name = username[0]
        game(name)


main()
