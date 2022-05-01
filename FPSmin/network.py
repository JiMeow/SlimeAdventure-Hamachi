import socket
import pickle

ips = {
    "Minzung": "25.31.231.0",
    "JiMeow": "25.34.159.172",
    "GolfGrab": "25.35.236.244"
    }
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(1)
        self.port = 3000
        self.ips = ips
        self.data = self.connect()
        self.id = str(self.data["id"])
        self.pos = self.data["pos"]

    def disconnect(self):
        self.client.close()

    def connect(self):
        for name,ip in self.ips.items():
            try:
                self.client.connect((ip, self.port))
                return pickle.loads(self.client.recv(128000))
            except:
                print(f"Connection to {name} failed")

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(128000))
        except socket.error as e:
            print(e)