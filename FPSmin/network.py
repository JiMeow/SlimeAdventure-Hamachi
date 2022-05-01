import socket
import pickle
from threading import Thread
from time import sleep

Minzung = "25.31.231.0"
JiMeow = "25.34.159.172"
GolfGrab = "25.35.236.244"
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 3000
        self.data = self.connect()
        self.id = str(self.data["id"])
        self.pos = self.data["pos"]

    def disconnect(self):
        self.client.close()

    def connect(self):
        thread = Thread(target=self.client.connect, args=((Minzung, self.port),))
        thread.start()
        sleep(3)
        if thread.is_alive():
            pass
            
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(128000))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(128000))
        except socket.error as e:
            print(e)
