import pygame
from threading import *
from setting import *
from collision import Collision
from layout import Layout
from network import Network
from map import Map
from ui import Login
import time


def redrawWindow(layout, p, allp, dt, collision, map, clock):
    """
    add all the elements to the layout
    for each element, draw it on the screen

    Args:
        layout (Layout): layout to add elements
        p (Player): information of player
        allp (List[Player]): information of all players
        dt (float): time between two frames
        collision (Collision): collision data
        map (Map): map data
    """
    layout.setCollision(collision)
    layout.setMap(map)
    layout.setPlayer(p)
    layout.setAllPlayer(allp)
    layout.setDt(dt)
    # Debug Fps
    layout.setDebug(f"{clock.get_fps():.2f}", 10, 10)
    layout.drawPlayerFrame()


def getDataP(network, p, tempallp=[], tempstatus={0: False, 1: False, 2: False, 3: False}):
    """
    get all data information from server and update them

    Args:
        network (_type_): _description_
        p (Player): _description_
        tempallp (List[Player], optional): list of information of all player . Defaults to [].
        tempstatus (dict, optional): which player are online. Defaults to {0: False, 1: False, 2: False, 3: False}.

    Returns:
        List[Player]: list of information of all player
        dict: which player are online
    """
    while(len(tempallp) != 0):
        tempallp.pop(0)
    data = network.send(p)
    tempallp += data["players"]
    for i in range(4):
        tempstatus[i] = data["status"][i]
    return tempallp, tempstatus


def exterpolation(p, allp, dt, collision, status, map):
    """
    predict the position of another players
    if data is not available but if the player is not 
    online, do nothing

    Args:
        p (Player): information of player
        allp (List[Player]): information of all players
        dt (float): time between two frames
        collision (Collision): collision data
        status (dict): which player are online
        map (Map): map data
    """
    for i in allp:
        if i.id != p.id and status[i.id-1]:
            i.jump(False, map.gravity, dt)
            collision.setPlayer(i)
            i.update(dt, collision)


def setNewCollision(p, allp, collision, map):
    """
    update new collision data

    Args:
        p (Player): information of player
        allp (List[Player]): information of all players
        collision (Collision): collision information for check collision.
        map (Map): _description_
    """
    collision.setPlayer(p)
    collision.setAllPlayer(allp)
    collision.setMap(map)


def setspawn(p, stage):
    """
    test by warp player to stage

    Args:
        p (Player): _description_
        stage (int): _description_
    """
    p.x = 30+width*stage
    return stage


def spawnpointAtEveryXstage(collision, stage, player):
    """
    set new spawn point for player at every x stage

    Args:
        collision (Collision): collision information
        stage (int): number of every x stage to set player spawn point
        player (Player): player information
    """
    collision.setSpawnStage(player.x//width//stage*stage)


def game(username):
    """
    run game with username by connecting to server
    and receive data from server then generate map
    and all player

    Args:
        username (str): name of player
    """
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Client")
    pygame.init()
    clock = pygame.time.Clock()

    run = True
    n = Network()
    p = n.getP()
    spawnpoint = setspawn(p, 0)
    p.name = username
    frame = 0
    map = Map(win, "JiMeow/photo/forest.png")

    allp, status = getDataP(n, p)
    tempallp = list(allp)
    tempstatus = dict(status)

    thread = Thread(target=getDataP, args=(n, p, tempallp))
    beforetime = time.time()
    layout = Layout(win)
    collision = Collision(p, allp, map, spawnpoint)

    # for bug player not fall
    p.jump(True, map.gravity, 1/60)

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
        redrawWindow(layout, p, allp, dt, collision, map, clock)
        spawnpointAtEveryXstage(collision, 5, p)
        frame += 1


def main():
    """
    show login window and run game when login successfully
    """
    username = []
    ui = Login(username)
    while(1):
        ui.show()
        name = username[0]
        game(name)


main()
