import socket
import pickle
from threading import Thread

ips = {
    "Minzung": "25.31.231.0",
    "JiMeow": "25.34.159.172",
    "GolfGrab": "25.35.236.244"
}


class Network:
    def __init__(self):
        # setup server data and environment ------------------------------------
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(1)
        self.port = 3000
        self.ips = ips
        self.data = self.connect()
        self.id = str(self.data["id"])
        self.pos = self.data["pos"]
        # setup data for client and server --------------------------------------
        self.server_data = {"player": {}}
        # setup thread ----------------------------------------------------------
        self.thread = Thread(target=self.get_server_data)

        # self.missing_frame = 0
        # self.get_server_data_time = 0

    def set_data(self, client_data):
        self.client_data = client_data
        self.set_client_data()

    def disconnect(self):
        self.client.close()

    def connect(self):
        for name, ip in self.ips.items():
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

    def get_server_data(self):
        if not self.thread.is_alive():
            self.thread = Thread(target=self._get_server_data)
            self.thread.start()
        #     print(self.missing_frame)
        #     self.get_server_data_time = 0
        #     self.missing_frame = 0
        # self.get_server_data_time += self.dt
        # self.missing_frame += 1

    def _get_server_data(self):
        self.server_data = self.send(self.client_data)

    def set_client_data(self, player=None):
        if player:
            self.client_data["pos"] = [*player.rect.center]
        else:
            self.client_data["pos"] = [*self.pos]
        self.client_data["id"] = self.id
        self.client_data["event"] = {"bullets": [], "target_pos": []}

    def validate_other_players(self, other_players):
        for k, v in tuple(other_players.items()):
            if k not in self.server_data["player"]:
                v.kill()
                del other_players[k]
