from src.setting import *


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


def getDataP(network, p, tempallp=[], tempstatus={}):
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
    for i in range(10):
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
    p.rect.x = p.x
    p.rect.y = p.y
    p.rect.width = p.width
    p.rect.height = p.height
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

def setdatafromserver(allp, status, tempallp, tempstatus):
    """
    set data from server

    Args:
        p (Player): _description_
    """
    while(len(allp) != 0):
        allp.pop(0)
    for i in tempallp:
        allp.append(i)
    for i in tempstatus:
        status[i] = tempstatus[i]