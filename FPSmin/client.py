import json
import pygame
from debug import debug
from glovar import *
from player import Player
from projectile import Projectile

width = 800
height = 800
        
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Client")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player_sprites = player_sprites
        self.projectile_sprites = projectile_sprites
        self.init_pos = network.getPos()
        self.player = Player(self.init_pos[0], self.init_pos[1], "green", control=True)
        self.id = network.id
        self.players = {}
        data["pos"] = [self.player.rect.centerx, self.player.rect.centery]
        data["event"] = {}
        
    def run(self):
        while self.running:
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    network.disconnect()
                    quit()
            
            self.screen.fill((100,100,200))
            res = network.send(data)
            data["pos"] = [self.player.rect.x,self.player.rect.y]
            data["event"] = {}
            print(f"[Recieve] {res}")
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
            self.player_sprites.update()
            self.projectile_sprites.update()
            self.player_sprites.draw(self.screen)
            self.projectile_sprites.draw(self.screen)
            
            
            
            
            
            
            debug(f"fps: {self.clock.get_fps()}",0,0)
            debug(f"move_durection: {self.player.move_direction.x:.2f},{self.player.move_direction.y:.2f}",0,10)
            debug(f"pos: {self.player.rect.x},{self.player.rect.y}",0,20)
            debug(f"face_direction: {self.player.face_direction.x},{self.player.face_direction.y}",0,30)
            debug(f"projectiles: {len(self.projectile_sprites)}",0,40)
            pygame.display.update()
    
    def network(self):
        pass
        
game = Game()
game.run()