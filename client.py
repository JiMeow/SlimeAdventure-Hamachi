import pygame
from threading import *
from src.setting import *
from src.collision import Collision
from src.ui import Login
from src.layout import Layout
from src.network import Network
from map import Map
import time
from utils.utils import *


def game(username, skinid):
    """
    run game with username by connecting to server
    and receive data from server then generate map
    and all player

    Args:
        username (str): name of player
    """
    win = pygame.display.set_mode((width, height))

    # win = pygame.Surface((width, height))
    # screen = pygame.display.set_mode((1920, 1080))

    pygame.display.set_caption("SlimeAdventure 2.0")
    pygame.init()
    clock = pygame.time.Clock()

    map = Map(win, "src/photo/forest.png")
    run = True
    n = Network()

    p, setdefaulttime = n.getP()
    map.timeoffset = time.time()-setdefaulttime

    p.skinid = skinid
    spawnpoint = setspawn(p, 0)
    p.name = username
    frame = 0

    allp, status = getDataP(n, p)
    tempallp = list(allp)
    tempstatus = dict(status)
    thread = Thread(target=getDataP, args=(n, p, tempallp))
    beforetime = time.time()
    layout = Layout(win)
    collision = Collision(p, allp, map, spawnpoint)

    # for bug player not fall
    p.jump(True, map.gravity, 1/60)
    p.jumpcount = 0

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
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    n.disconnect()
                    break

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
        redrawWindow(layout, p, allp, dt, collision, map, clock)
        spawnpointAtEveryXstage(collision, 5, p)
        frame += 1
        # screen.blit(pygame.transform.scale(win, (1920, 1080)), (0, 0))


def main():
    """
    show login window and run game when login successfully
    """
    # username = ["q", 1]
    username = []
    ui = Login(username)
    while(1):
        ui.show()
        name = username[0]
        skinid = username[1]
        game(name, skinid)
    print("Thanks for playing")


main()
