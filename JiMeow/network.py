import socket
import pickle


server = "25.34.159.172"  # JiMeow
# server = "25.35.236.244" # GolfGrab
# server = "25.31.231.0" # Minzung
port = 5555


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def disconnect(self):
        self.client.close()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(65536))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(65536))
        except socket.error as e:
            print(e)
