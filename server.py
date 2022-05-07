import socket
import json
import time
from threading import *
import pickle

import pygame
from src.player import Player
from src.setting import *
import hashlib


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)
    
s.listen(20)
print("Waiting for a connection, Server Started")
maxPlayers = 10

players = []
for i in range(maxPlayers):
    players.append(Player(i+1, 30, -100, 50, 34, (0, 0, 0), f"Player{i+1}"))

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
    username, password = pickle.loads(conn.recv(65536))
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(player,":",username,"connected")
    
    login = False
    with open("data.json", "r") as f:
        r = json.load(f)
        if username in r:
            if r[username]["password"] == hashed_password:     
                login = True
                conn.send(pickle.dumps(("success login",r[username]["stage"])))
            else:    
                conn.send(pickle.dumps(("username already in use or incorrect password",0)))
        if username not in r:
            login = True
            conn.send(pickle.dumps(("account created",0)))
            r[username] = {"password":hashed_password, "stage":0}
    
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
        
    print(f"{username} Lost connection")
    if login:
        with open("data.json", "w") as f:
            r[username]["stage"] =  int(players[player].x)//width
            json.dump(r, f)
    currentPlayer[player] = 0
    players[player].x = 30
    players[player].y = -100
    players[player].rect = pygame.Rect(30, -100, 54, 30)
    conn.close()


def main():
    """
    start server wait for client to connect
    and check number of player and decide 
    which client will be which id
    """
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
        thread.start()
    
main()