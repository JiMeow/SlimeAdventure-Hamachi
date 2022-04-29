import pygame
from _thread import *
from network import Network
import json

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

pygame.init()
font = pygame.font.Font(None, 20)


def debug(info, x, y):
    screen = pygame.display.get_surface()
    text = font.render(str(info), True, "White")
    rect = text.get_rect(topleft=(x, y))
    pygame.draw.rect(screen, "Black", rect)
    screen.blit(text, rect)


class Player():
    def __init__(self, x, y, width, height, color, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3
        self.name = name

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def drawname(self, win):
        text = font.render(str(self.name), True, "White")
        rect = text.get_rect(topleft=(self.x, self.y))
        win.blit(text, rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return tup


def make_data(player1):
    send = {}
    send["pos"] = make_pos((player1.x, player1.y))
    send["name"] = player1.name
    # print(send)
    return json.dumps(send)+"|"


def redrawWindow(win, player1, player2, player3, player4, playername):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    player3.draw(win)
    player4.draw(win)
    namevar = 2
    for i in "1234":
        if i == str(playername+1):
            eval("player1").drawname(win)
        else:
            eval("player"+str(namevar)).drawname(win)
            namevar += 1


def getDataP(network, player1, player2, player3, player4, playername):
    pData = network.send(make_data(player1))
    pData = json.loads(pData)
    name = 1
    # print(pData)
    for i in "1234":
        # if i == str(nowplayer+1):
        #     continue
        if i == str(playername+1):
            continue
        else:
            name += 1
            pos = read_pos(pData[i]["pos"])
            eval("player"+str(name)).x, eval("player" +
                                             str(name)).y = pos
            eval("player"+str(name)).name = pData[i]["name"]
            eval("player"+str(name)).update()


def main():
    run = True
    n = Network()
    username = input("Username: ")
    # print(n.getPos())
    startPos = read_pos(n.getPos())
    playername = int(n.send("GetName"))
    p1 = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0), username)
    p2 = Player(0, 0, 100, 100, (255, 0, 0), "player2")
    p3 = Player(0, 0, 100, 100, (255, 0, 0), "player3")
    p4 = Player(0, 0, 100, 100, (255, 0, 0), "player4")
    clock = pygame.time.Clock()
    frame = 0
    while run:

        clock.tick(60)
        if frame % 4 == 0:
            start_new_thread(getDataP, (n, p1, p2, p3, p4, playername))
        # p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        # p2.x = p2Pos[0]
        # p2.y = p2Pos[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redrawWindow(win, p1, p2, p3, p4, playername)
        debug(clock.get_fps(), 0, 0)
        # debug(f"{p.x},{p.y}", 0, 10)
        # debug(f"{p2.x},{p2.y}", 0, 20)
        pygame.display.update()

        frame += 1


main()
