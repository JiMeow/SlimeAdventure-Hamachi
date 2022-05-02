import pygame
from threading import Thread
from debug import debug
from glovar import *
from settings import *
from network import Network
from player import Player
from projectile import Projectile

# done
# right click to walk
# connection timeout socket.settimeout
# camera lock

# done?
# interpolation
# exterpolation

# to do
# walk point image
# map
# offset mouse target point
# camera follow by mouse
# select server

# select elements qwer asdf 8 elements
# ui Ex : hp, mp, exp, level, skill point, skill list
# element : water, heal, shield, ice, thunder, death, stone, fire  
# skill : fast walk, revive, reaper, metor shower

# left click shoot
# middle click use to yourself
# right click walk

# element iteration like fire + water
# health damage stun slow fire ice falling knockback    
# when cast should lock speed to rotate face direction

# server validation data


class Layer:
    def __init__(self,**kwargs):
        self.screen = pygame.display.get_surface()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.offset = pygame.math.Vector2()
        # background setup
        self.background_image = pygame.Surface((400,100))
        self.background_image.fill("red")
        self.background_rect = self.background_image.get_rect(topleft=(0,0))
        # sprite groups
        self.player_sprites = player_sprites
        self.projectile_sprites = projectile_sprites
        self.all_sprites = [self.player_sprites, self.projectile_sprites]
        # box setup
        self.camera_boarders = {"left": 200, "right": 200, "top": 200, "bottom": 200}
        l = self.camera_boarders["left"]
        t = self.camera_boarders["top"]
        w = self.width - self.camera_boarders["right"] - self.camera_boarders["left"]
        h = self.height - self.camera_boarders["bottom"] - self.camera_boarders["top"]
        self.camera_rect = pygame.Rect(l,t,w,h)
        
    def render(self,player,dt):
        self.update(dt)
        
        self.screen.fill(background_color)
        self.camera_render(player)
        # self.default_render(player)
    
    def default_render(self,player):
        self.screen.blit(self.background_image, self.background_rect)
        player.draw_cursor(self.screen)
        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect)
    
    def update(self,dt):
        self.player_sprites.update(dt)
        self.projectile_sprites.update(dt)

    def sprites(self):
        sprites = []
        for group in self.all_sprites:
            sprites += group.sprites()
        return sprites
    
    def camera_render(self,player):
        
        self.offset.x = player.rect.centerx - self.width//2
        self.offset.y = player.rect.centery - self.height//2
        
        #test object
        offset_pos = self.background_rect.topleft - self.offset
        self.screen.blit(self.background_image, offset_pos)
        #all sprites
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            if sprite == player:
                continue
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)
        pygame.draw.rect(self.screen, "yellow", self.camera_rect, 5)
        #cursor
        player.draw_cursor(self.screen, self.offset)
        #player
        offset_pos = player.rect.topleft - self.offset
        self.screen.blit(player.image, offset_pos)
        
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Client")
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.layer = Layer()
        self.running = True
        
        self.network = Network()
        self.id = self.network.id
        self.player = Player(self.network.pos[0], self.network.pos[1], "green", name="player "+self.id, control=True)
        
        # setup data and thread
        self.set_client_data(init=True)
        
        self.old_server_data = None
        self.server_data = {"player": {}}
        self.other_players = {}
        
        self.thread = Thread(target=self.get_server_data)

        self.missing_frame = 0
        self.get_server_data_dt = 0
        
    def get_server_data(self):
        
        if not self.thread.is_alive():
            self.thread = Thread(target=self._get_server_data)
            self.thread.start()
            self.interpolation_dt = self.get_server_data_dt
            self.get_server_data_dt = 0
            # print(self.missing_frame)
            self.missing_frame = 0
        self.get_server_data_dt += self.dt
        self.missing_frame += 1
        
    def _get_server_data(self):
        self.old_server_data = self.server_data
        self.server_data = self.network.send(self.client_data)
    
    def set_client_data(self, init=False):
        if init:
            self.client_data = client_data
        self.client_data["pos"] = [self.player.rect.centerx,self.player.rect.centery]
        self.client_data["id"] = self.id
        self.client_data["event"] = {"bullets":[],"target_pos":[]}
        
    def validate_other_players(self): # validate other players to matched with server data
        for k,v in tuple(self.other_players.items()):
            if k not in self.server_data["player"]:
                v.kill()
                del self.other_players[k]
    
    def update_stc(self):
        self.validate_other_players()
        for player_id,player in self.server_data["player"].items():
            if player_id == self.id:
                continue
            if player_id in self.other_players:
                if player["event"]["bullets"]:
                    bullets = player["event"]["bullets"]
                    for bullet in bullets:
                        face_direction = pygame.math.Vector2(bullet["direction"][0], bullet["direction"][1])
                        Projectile(bullet["pos"][0], bullet["pos"][1], face_direction)
                if player["event"]["target_pos"]:
                    self.other_players[player_id].target_pos = player["event"]["target_pos"]
            else:
                self.other_players[player_id] = Player(player["pos"][0], player["pos"][1], "red", name="player "+player_id)
    
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.network.disconnect()
                pygame.quit()
    
    def run(self):
        while self.running:
            self.clock.tick(fps)
            self.dt = (self.clock.get_time() * fps) / 1000
            
            self.event_handler()
            
            self.get_server_data()
            self.update_stc()
            self.set_client_data()
            
            self.layer.render(self.player, self.dt)

            self.display_debug()
            
            pygame.display.update()
            
    def display_debug(self):
        self.debug_count = [0]
        debug(f"fps: {self.clock.get_fps():.2f}", self.debug_count)
        debug(f"pos: {self.player.rect.centerx},{self.player.rect.centery}", self.debug_count)
        debug(f"move_durection: {self.player.move_direction.x:.2f},{self.player.move_direction.y:.2f}", self.debug_count)
        debug(f"face_direction: {self.player.face_direction.x:.2f},{self.player.face_direction.y:.2f}", self.debug_count)
        debug(f"face_angle: {self.player.face_direction.angle_to(pygame.math.Vector2(1, 0)):.2f}",self.debug_count)
        debug(f"target_pos: {self.player.target_pos[0]},{self.player.target_pos[1]}", self.debug_count)
        debug(f"players: {len(self.layer.player_sprites.sprites())}", self.debug_count)
        debug(f"projectiles: {len(self.layer.projectile_sprites.sprites())}", self.debug_count)
        


game = Game()
game.run()