import pygame
from debug import debug
from glovar import *
from player import Player
from projectile import Projectile
from threading import Thread
from network import Network

width = 800
height = 800
        
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Client")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.network = Network()
        self.init_pos = self.network.pos
        self.id = self.network.id
        self.players = {}
        
        self.player = Player(self.init_pos[0], self.init_pos[1], "green", control=True)
        self.player_sprites = player_sprites
        self.projectile_sprites = projectile_sprites
        
        self.client_data = client_data
        self.client_data["pos"] = [self.player.rect.centerx,self.player.rect.centery]
        self.client_data["event"] = {}
        
        
    def run(self):
        while self.running:
            self.clock.tick(60)
            dt = self.clock.get_time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.network.disconnect()
                    pygame.quit()
            
            self.screen.fill((100,100,200))
            res = self.network.send(self.client_data)
            self.client_data["pos"] = [self.player.rect.x,self.player.rect.y]
            self.client_data["event"] = {}
            # print(f"[Recieve] {res}")
            for k,v in res["player"].items():
                if k == self.id:
                    continue
                if k in self.players:
                    self.players[k].rect.x = v["pos"][0]
                    self.players[k].rect.y = v["pos"][1]
                    if v["event"]:
                        face_direction = pygame.math.Vector2(v["event"]["direction"][0], v["event"]["direction"][1])
                        Projectile(v["event"]["pos"][0], v["event"]["pos"][1], face_direction)
                else:
                    self.players[k] = Player(v["pos"][0], v["pos"][1], "red")
            self.player_sprites.update(dt)
            self.projectile_sprites.update(dt)
            self.player_sprites.draw(self.screen)
            self.projectile_sprites.draw(self.screen)
            
            
            
            
            
            
            debug(f"fps: {self.clock.get_fps()}",0,0)
            debug(f"move_durection: {self.player.move_direction.x:.2f},{self.player.move_direction.y:.2f}",0,10)
            debug(f"pos: {self.player.rect.x},{self.player.rect.y}",0,20)
            debug(f"face_direction: {self.player.face_direction.x},{self.player.face_direction.y}",0,30)
            debug(f"projectiles: {len(self.projectile_sprites)}",0,40)
            pygame.display.update()
        
game = Game()
game.run()