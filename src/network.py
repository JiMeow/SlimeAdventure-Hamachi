import socket
import pickle
from src.player import Player
from src.setting import *


class Network:
    def __init__(self):
        """
        set default value of network for multiplayer game
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        """
        get player information from server

        Returns:
            Player: player information
        """
        return self.p

    def disconnect(self):
        """
        disconnect from server
        """
        self.client.close()

    def connect(self):
        """
        get first information from server

        Returns:
            Player: player information
        """
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(65536))
        except Exception as e:
            print(e)

    def send(self, data):
        """
        send data then receive data from server

        Args:
            data (Player): player information

        Returns:
            dict: information of all data from server
        """
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(65536))
        except socket.error as e:
            print(e)
