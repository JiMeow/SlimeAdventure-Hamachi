import pygame
from debug import debug
from glovar import *
from player import Player
from projectile import Projectile
from threading import Thread
from network import Network
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Client")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.network = Network()
        self.id = self.network.id
        self.other_players = {}

        self.player = Player(self.network.pos[0], self.network.pos[1], "green", control=True)
        self.player_sprites = player_sprites
        self.projectile_sprites = projectile_sprites
        
        self.client_data = client_data
        self.client_data["pos"] = [self.player.rect.centerx,self.player.rect.centery]
        self.client_data["event"] = {}
        
        self.thread = Thread(target=self.get_server_data)
        self.server_data = {"player":{}}
    
    def get_server_data(self):
        self.server_data = self.network.send(self.client_data)
    
    def check_other_players(self):
        for k,v in tuple(self.other_players.items()):
            if k not in self.server_data["player"]:
                v.kill()
                del self.other_players[k]
    
    def update(self):
        self.check_other_players()
        for k,v in self.server_data["player"].items():
            if k == self.id:
                continue
            if k in self.other_players:
                self.other_players[k].rect.x = v["pos"][0]
                self.other_players[k].rect.y = v["pos"][1]
                if v["event"]:
                    bullets = v["event"]["bullets"]
                    for bullet in bullets:
                        face_direction = pygame.math.Vector2(bullet["direction"][0], bullet["direction"][1])
                        Projectile(bullet["pos"][0], bullet["pos"][1], face_direction)
            else:
                self.other_players[k] = Player(v["pos"][0], v["pos"][1], "red")
        
    def run(self):
        while self.running:
            self.clock.tick(fps)
            dt = self.clock.get_time()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.network.disconnect()
                    pygame.quit()
            
            if not self.thread.is_alive():
                self.thread = Thread(target=self.get_server_data)
                self.thread.start()
            
            self.update()
            self.client_data["pos"] = [self.player.rect.x,self.player.rect.y]
            self.client_data["event"] = {"bullets":[]}
            # print(f"[Recieve] {server_data}")
            
            self.screen.fill((100,100,200))
            self.player_sprites.update(dt)
            self.projectile_sprites.update(dt)
            self.player_sprites.draw(self.screen)
            self.projectile_sprites.draw(self.screen)
            
            debug(f"fps: {self.clock.get_fps():.2f}",0,0)
            debug(f"move_durection: {self.player.move_direction.x:.2f},{self.player.move_direction.y:.2f}",0,10)
            debug(f"pos: {self.player.rect.x},{self.player.rect.y}",0,20)
            debug(f"face_direction: {self.player.face_direction.x:.2f},{self.player.face_direction.y:.2f}",0,30)
            debug(f"players: {len(self.player_sprites.sprites())}",0,40)
            debug(f"projectiles: {len(self.projectile_sprites.sprites())}",0,50)
            
            pygame.display.update()
        
game = Game()
game.run()