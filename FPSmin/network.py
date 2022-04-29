import socket
import json
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "25.31.231.0"
        self.port = 3000
        self.addr = (self.server, self.port)
        self.tmp = self.connect()
        print(self.tmp)
        self.id = str(self.tmp["id"])
        self.pos = self.tmp["pos"]

    def getPos(self):
        return self.pos

    def disconnect(self):
        self.client.close()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(64000))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(64000))
        except socket.error as e:
            print(e)