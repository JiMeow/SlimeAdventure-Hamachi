import socket
from _thread import *
import pickle

ip = "25.34.159.172"
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(10)
print("Start!")

data = {"player": {}}

server_player_ID = 1
start_pos = [100, 100]


def recv_data(conn):
    return pickle.loads(conn.recv(60000))


def send_data(conn, send):
    conn.send(pickle.dumps(send))


def threaded_client(conn):
    global server_player_ID

    player_ID = str(server_player_ID)

    data["player"][player_ID] = {}
    data["player"][player_ID]["pos"] = start_pos
    data["player"][player_ID]["id"] = player_ID
    data["player"][player_ID]["event"] = {}
    res = data["player"][player_ID]
    print(f"[Sending] p{player_ID}: {res}")
    send_data(conn, res)
    server_player_ID += 1

    while True:
        try:
            recv = recv_data(conn)
            print(f"[Recieve] p{player_ID}: {recv}")
            data["player"][player_ID]["pos"] = recv["pos"]
            data["player"][player_ID]["event"] = recv["event"]
            print(f"[Sending] p{player_ID}: {data}")
            send_data(conn, data)

        except:
            print(f"{player_ID} Lost connection")
            break

    del data["player"][player_ID]
    server_player_ID -= 1

    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,))
