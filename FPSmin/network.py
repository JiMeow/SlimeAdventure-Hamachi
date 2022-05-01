import socket
import pickle

# server = "25.34.159.172"  # JiMeow
# server = "25.35.236.244" # GolfGrab
server = "25.31.231.0"  # Minzung


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = 3000
        self.addr = (self.server, self.port)
        self.data = self.connect()
        self.id = str(self.data["id"])
        self.pos = self.data["pos"]

    def disconnect(self):
        self.client.close()

    def connect(self):
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
