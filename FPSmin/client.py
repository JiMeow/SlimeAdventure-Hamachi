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
        # box setup [nessary]
        self.camera_boarders = {"left": 200, "right": 200, "top": 200, "bottom": 200}
        l = self.camera_boarders["left"]
        t = self.camera_boarders["top"]
        w = self.width - self.camera_boarders["right"] - self.camera_boarders["left"]
        h = self.height - self.camera_boarders["bottom"] - self.camera_boarders["top"]
        self.camera_rect = pygame.Rect(l,t,w,h)
        # zoom setup [optional]
        self.keyboard_speed = 5
        self.mouse_speed = 0.4
        self.zoom_scale = 1
        self.min_zoom_scale = 0.5
        self.max_zoom_scale = 2
        self.internal_surface_size = (self.width * 1/self.min_zoom_scale, self.height * 1/self.min_zoom_scale)
        self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surface.get_rect(center = (self.width//2,self.height//2))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surface_size[0] // 2 - self.width // 2
        self.internal_offset.y = self.internal_surface_size[1] // 2 - self.height // 2
        
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
    
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.width//2
        self.offset.y = target.rect.centery - self.height//2
    
    def box_target_camera(self,target):
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom
            
        self.offset.x = self.camera_rect.left - self.camera_boarders["left"]
        self.offset.y = self.camera_rect.top - self.camera_boarders["top"]
    
    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.offset.x -= self.keyboard_speed
        if keys[pygame.K_d]:
            self.offset.x += self.keyboard_speed
        if keys[pygame.K_w]:
            self.offset.y -= self.keyboard_speed
        if keys[pygame.K_s]:
            self.offset.y += self.keyboard_speed
    
    def mouse_control(self):
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_offset_vector = pygame.math.Vector2()
        
        left_border = self.camera_boarders["left"]
        top_border = self.camera_boarders["top"]
        right_border = self.width - self.camera_boarders["right"]
        bottom_border = self.height - self.camera_boarders["bottom"]
        
        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector.x = mouse.x - left_border
                pygame.mouse.set_pos(left_border, mouse.y)
            if mouse.x > right_border:
                mouse_offset_vector.x = mouse.x - right_border
                pygame.mouse.set_pos(right_border, mouse.y)
        elif mouse.y < top_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border, top_border)
                pygame.mouse.set_pos(left_border, top_border)
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border, top_border)
                pygame.mouse.set_pos(right_border, top_border)
        elif mouse.y > bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border, bottom_border)
                pygame.mouse.set_pos(left_border, bottom_border)
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border, bottom_border)
                pygame.mouse.set_pos(right_border, bottom_border)
            
        if left_border < mouse.x < right_border:
            if mouse.y < top_border:
                mouse_offset_vector.y = mouse.y - top_border
                pygame.mouse.set_pos(mouse.x, top_border)
            if mouse.y > bottom_border:
                mouse_offset_vector.y = mouse.y - bottom_border
                pygame.mouse.set_pos(mouse.x, bottom_border)
        
        self.offset += mouse_offset_vector * self.mouse_speed
    
    def zoom_keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.zoom_scale += 0.1
        if keys[pygame.K_e]:
            self.zoom_scale -= 0.1
        if self.zoom_scale < self.min_zoom_scale:
            self.zoom_scale = self.min_zoom_scale
        if self.zoom_scale > self.max_zoom_scale:
            self.zoom_scale = self.max_zoom_scale
            

    def pre_zoom(self):
        self.zoom_keyboard_control()
        self.offset -= self.internal_offset
        self.internal_surface.fill(background_color)
        self.surface = self.internal_surface
        
    def post_zoom(self):
        scaled_surface = pygame.transform.scale(self.internal_surface,self.internal_surface_size_vector*self.zoom_scale)
        scaled_rect = scaled_surface.get_rect(center = (self.width//2,self.height//2))
        self.screen.blit(scaled_surface, scaled_rect)
        
    def camera_render(self,player):
        self.surface = self.screen
        self.center_target_camera(player)
        # self.box_target_camera(player)
        # self.keyboard_control()
        # self.mouse_control()
        self.pre_zoom()
        
        #test object
        offset_pos = self.background_rect.topleft - self.offset
        self.surface.blit(self.background_image, offset_pos)
        #all sprites
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            if sprite == player:
                continue
            offset_pos = sprite.rect.topleft - self.offset
            self.surface.blit(sprite.image, offset_pos)
        # draw camera block
        # pygame.draw.rect(self.surface, "yellow", self.camera_rect, 5)
        #cursor
        player.draw_cursor(self.surface, self.offset)
        #player
        offset_pos = player.rect.topleft - self.offset
        self.surface.blit(player.image, offset_pos)
        
        self.post_zoom()
                
class Game:
    def __init__(self):
        pygame.init()
        pygame.event.set_grab(True)
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
            if event.type == pygame.MOUSEWHEEL:
                self.layer.zoom_scale += event.y * 0.03
    
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