import pygame


class PlayerGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def get_player(self):
        for player in self.sprites():
            if player.control:
                return player
