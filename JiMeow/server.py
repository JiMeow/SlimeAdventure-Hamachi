import socket
from threading import *
import pickle
from player import Player

server = "25.34.159.172"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(20)
print("Waiting for a connection, Server Started")


players = [Player(1, 0, 0, 50, 50, (255, 0, 0), "Player1"), Player(2, 100, 100, 50, 50, (0, 255, 0), "Player2"),
           Player(3, 200, 200, 50, 50, (0, 0, 255), "Player3"), Player(4, 300, 300, 50, 50, (255, 255, 0), "Player4")]


def threaded_client(conn, player):
    # print("I Try")
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(65536))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = players

            conn.sendall(pickle.dumps(reply))
        except:
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
    # print("WTF")
    thread = Thread(target=threaded_client, args=(conn, idx))
    print(idx, "Connected to:", addr)
    thread.start()
