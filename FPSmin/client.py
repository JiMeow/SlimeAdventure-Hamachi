import pygame
from settings import *
from debug import debug
from layer import Layer
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
# when cast should slow speed to rotate face direction

# server validation data


class Game:
    def __init__(self):
        # setup game ------------------------------------------------------------
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Client")
        # pygame.event.set_grab(True)
        self.clock = pygame.time.Clock()
        self.running = True
        # setup sprites and layer ------------------------------------------------
        self.player_sprites = pygame.sprite.Group()
        self.projectile_sprites = pygame.sprite.Group()
        self.all_sprites_group = {
            "player": self.player_sprites,
            "projectile": self.projectile_sprites
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
            if player["event"]["bullets"]:
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
            if event.type == pygame.QUIT:
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
            self.layer.render(self.player)
            # display debug ------------------------------------------------------
            self.display_debug()
            # pygame display update ----------------------------------------------
            pygame.display.update()

    def display_debug(self):
        self.debug_count = [0]
        debugs = [
            f"fps: {self.clock.get_fps():.2f}",
            f"pos: {self.player.rect.centerx},{self.player.rect.centery}",
            f"move_durection: {self.player.move_direction.x:.2f},{self.player.move_direction.y:.2f}",
            f"face_direction: {self.player.face_direction.x:.2f},{self.player.face_direction.y:.2f}",
            f"face_angle: {self.player.face_direction.angle_to(pygame.math.Vector2(1, 0)):.2f}",
            f"target_pos: {self.player.target_pos[0]},{self.player.target_pos[1]}",
            f"players: {len(self.player_sprites.sprites())}",
            f"projectiles: {len(self.projectile_sprites.sprites())}"
        ]
        for text in debugs:
            debug(text, self.debug_count)


game = Game()
game.run()
