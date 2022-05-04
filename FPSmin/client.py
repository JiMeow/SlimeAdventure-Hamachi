import pygame
from settings import *
from debug import debug
from layer import Layer
from network import Network
from player import Player
from playergroup import PlayerGroup
from projectile import Projectile
from tile import Tile
import random
# done
# right click to walk
# connection timeout socket.settimeout
# camera lock
# camera follow by mouse
# slow speed when cast
# offset mouse target point

# done?
# interpolation
# exterpolation

# to do
# walk point image
# map
# projectile author
# slow other player
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
# when cast should slow speed and speed rotate face direction

# server validation data

# refactor update_stc, other player slow walk
# refactor camera follow by mouse
# refactor circle


class Circle(pygame.sprite.Sprite):
    def __init__(self, group, radius, angle, color):
        super().__init__(group)
        self.real_image = pygame.Surface((2, 2)).convert()
        self.real_image.set_colorkey((0, 0, 0))
        self.real_image.fill(color)
        self.real_image_rect = self.real_image.get_rect(topleft=(0, 0))
        self.image = pygame.Surface((radius*2, 2)).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.real_image, self.real_image_rect)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(width//2, height//2))


class Game:
    def __init__(self):
        # setup game ------------------------------------------------------------
        pygame.init()
        self.screen = pygame.display.set_mode(
            (width, height),
        )
        pygame.display.set_caption("Client")
        # pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.running = True
        # setup sprites and layer ------------------------------------------------
        self.player_sprites = PlayerGroup()
        self.projectile_sprites = pygame.sprite.Group()
        self.tile_sprites = pygame.sprite.Group()
        t = pygame.time.get_ticks()
        for x in range(-2000, 2001, tile_image_size[0]):
            for y in range(-2000, 2001, tile_image_size[1]):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                Tile(
                    self.tile_sprites,
                    pos=(x, y),
                    color=(r, g, b),
                )
        t1 = pygame.time.get_ticks() - t
        self.circle_sprites = pygame.sprite.Group()
        # for i in range(720):
        #     Circle(self.circle_sprites, small_cir_rad, i/2, "yellow")
        #     Circle(self.circle_sprites, big_cir_rad, i/2, "red")
        t2 = pygame.time.get_ticks() - t
        self.all_sprites_group = {
            "tile": self.tile_sprites,
            "circle": self.circle_sprites,
            "projectile": self.projectile_sprites,
            "player": self.player_sprites,
        }
        self.layer = Layer(self.all_sprites_group)
        # setup network ---------------------------------------------------------
        self.client_sending_data = {}
        self.client_data = {"player": {}}
        self.network = Network(self.client_sending_data)
        self.id = self.network.id
        # setup player ----------------------------------------------------------
        self.player = Player(
            pos=self.network.pos,
            color="green",
            name="player " + self.id,
            control=True,
            client_sending_data=self.client_sending_data,
            all_sprites_group=self.all_sprites_group
        )
        self.layer.camera.set_player()
        self.player.set_pcmc_vec(self.layer.camera.pcmc_vec)
        print(t1, t2)
    # this func need to refactor

    def update_stc(self):
        # prepare data from server
        self.server_data = self.network.server_data
        self.network.update_client_data(self.client_data)
        # update data from server to client
        player_client_data = self.client_data["player"]
        for player_id, player in player_client_data.items():
            if player["player"] == None:
                player["player"] = Player(
                    pos=player["pos"],
                    color="red",
                    name="player " + player_id,
                    all_sprites_group=self.all_sprites_group
                )
            player["player"].is_shoot = False
            if player["event"]["bullets"]:
                player["player"].is_shoot = True
                bullets = player["event"]["bullets"]
                for bullet in bullets:
                    face_direction = pygame.math.Vector2(*bullet["direction"])
                    Projectile(
                        bullet["pos"],
                        face_direction,
                        all_sprites_group=self.all_sprites_group
                    )
            if player["event"]["target_pos"]:
                player["player"].target_pos = player["event"]["target_pos"]

    def network_update(self):
        # get data from server
        self.network.get_server_data()
        # update data from server to client
        self.update_stc()
        # set sending data for sending to server
        self.network.set_client_sending_data(self.player)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
                self.network.disconnect()
                # pygame.quit()
            if event.type == pygame.MOUSEWHEEL:
                self.layer.camera.zoom_scale += event.y * 0.03

    def run(self):
        while self.running:
            # game tick ----------------------------------------------------------
            self.clock.tick(fps)
            # pygame event -------------------------------------------------------
            self.event_handler()
            # client data and server data ----------------------------------------
            self.network_update()
            # render layer -------------------------------------------------------
            self.layer.render()
            # display debug ------------------------------------------------------
            self.display_debug()
            # pygame display update ----------------------------------------------
            pygame.display.update()

    def display_debug(self):
        self.debug_count = [0]
        debugs = [
            f"fps: {self.clock.get_fps():.2f}",
            f"pos: {self.player.rect.centerx},{self.player.rect.centery}",
            f"target_pos: {self.player.target_pos[0]},{self.player.target_pos[1]}",
            f"mouse_pos: {pygame.mouse.get_pos()}",
            f"move_durection: {self.player.move_direction.x:.2f},{self.player.move_direction.y:.2f}",
            f"face_direction: {self.player.face_direction.x:.2f},{self.player.face_direction.y:.2f}",
            f"face_angle: {self.player.face_direction.angle_to(pygame.math.Vector2(1, 0)):.2f}",
            f"players: {len(self.player_sprites.sprites())}",
            f"projectiles: {len(self.projectile_sprites.sprites())}"
        ]
        for text in debugs:
            debug(text, self.debug_count)


game = Game()
game.run()
