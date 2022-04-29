import socket
from _thread import *
import sys
from pyngrok import ngrok
import json

server = "25.34.159.172"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(20)
print("Waiting for a connection, Server Started")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1]) + ","


def reply_data(player):
    reply = {}
    for i in range(maxPlayers):
        reply[i+1] = {
            "pos": make_pos(pos[i]),
            "name": playername[i]
        }
    return json.dumps(reply)


pos = [(0, 0), (400, 0), (0, 400), (400, 400), ]
playername = ["player1", "player2", "player3", "player4"]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    temp = conn.recv(65536).decode()
    conn.send(str.encode(str(player)))

    reply = ""
    while True:
        try:
            data = conn.recv(65536).decode()
            data = data.split("|")[0]
            data = json.loads(data)
            # print(data)
            # pos[player] = read_pos(data["pos"])
            pos[player] = (int(data["pos"][0]), int(data["pos"][1]))
            # print(data)
            playername[player] = data["name"]
            # print(data)

            if not data:
                print("Disconnected")
                break
            else:
                reply = reply_data(player)
            # print(data)
            conn.sendall(str.encode(reply))
        except:
            print(data)
            break
    print(f"{player} Lost connection")
    global currentPlayer
    currentPlayer[player] = 0
    conn.close()


maxPlayers = 4
currentPlayer = {}
for i in range(maxPlayers):
    currentPlayer[i] = 0
idx = 0
while True:
    conn, addr = s.accept()
    for i in range(maxPlayers):
        if currentPlayer[i] == 0:
            currentPlayer[i] = 1
            idx = i
            break
    print(idx, "Connected to:", addr)
    start_new_thread(threaded_client, (conn, idx))
