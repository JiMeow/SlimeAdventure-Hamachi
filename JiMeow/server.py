import socket
import time
from threading import *
import pickle
from player import Player
from setting import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(20)
print("Waiting for a connection, Server Started")

players = [Player(1, 30, -100, 50, 34, (255, 0, 0), "Player1"), Player(2, 30, -100, 50, 34, (0, 255, 0), "Player2"),
           Player(3, 30, -100, 50, 34, (0, 0, 255), "Player3"), Player(4, 30, -100, 50, 34, (255, 0, 255), "Player4")]

currentPlayer = {}


def threaded_client(conn, player):
    """
    start thread for each client to receive data from server

    Args:
        conn (socket): connection from client
        player (int): id of player
    """
    global currentPlayer
    conn.send(pickle.dumps((players[player], time.time())))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(65536))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = {"players": players,
                         "status": currentPlayer}

            conn.sendall(pickle.dumps(reply))
        except:
            break
    print(f"{player} Lost connection")
    currentPlayer[player] = 0
    players[player].x = 30
    players[player].y = -100
    conn.close()


def main():
    """
    start server wait for client to connect
    and check number of player and decide 
    which client will be which id
    """
    maxPlayers = 4
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
        thread = Thread(target=threaded_client, args=(conn, idx))
        print(idx, "Connected to:", addr)
        thread.start()


main()
