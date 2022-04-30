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

        self.player = Player(self.network.pos[0], self.network.pos[1], "green", name="player "+self.id, control=True)
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
    
    def update_stc(self):
        self.check_other_players()
        for player_id,player in self.server_data["player"].items():
            if player_id == self.id:
                continue
            if player_id in self.other_players:
                self.other_players[player_id].rect.x = player["pos"][0]
                self.other_players[player_id].rect.y = player["pos"][1]
                if player["event"]:
                    bullets = player["event"]["bullets"]
                    for bullet in bullets:
                        face_direction = pygame.math.Vector2(bullet["direction"][0], bullet["direction"][1])
                        Projectile(bullet["pos"][0], bullet["pos"][1], face_direction)
            else:
                self.other_players[player_id] = Player(player["pos"][0], player["pos"][1], "red", name="player "+player_id)
    
    def reset_client_data(self):
        self.client_data["pos"] = [self.player.rect.x,self.player.rect.y]
        self.client_data["event"] = {"bullets":[]}
    
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
            
            self.update_stc()
            self.reset_client_data()
            # print(f"[Recieve] {server_data}")
            
            self.screen.fill(background_color)
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