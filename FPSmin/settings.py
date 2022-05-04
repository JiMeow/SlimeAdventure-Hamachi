import pygame
from utils.utils import *

pygame.init()
font = pygame.font.Font(None, 20)


fps = 60
width = 800
height = 800
# width = 1920
# height = 1080
small_cir_rad = width//4
big_cir_rad = width//2
# make it can load image
pygame.display.set_mode((width, height))
background_color = (100, 100, 200)
gb_colorkey = (1, 1, 1)
# player settings
player_image_size = (50, 50)

player_image_path_green = "FPSmin/assets/green.png"
player_image_green = load_img(
    player_image_path_green, gb_colorkey, player_image_size
)

player_image_path_red = "FPSmin/assets/red.png"
player_image_red = load_img(
    player_image_path_red, gb_colorkey, player_image_size
)

player_cursor_size = (25, 15)
player_cursor_image_path = "FPSmin/assets/mouse/pos"
player_cursor_images = load_ani(
    player_cursor_image_path, (0, 0, 0), player_cursor_size
)

player_fast_speed = 8
player_normal_speed = 5
player_slow_speed = 3
player_rotation_speed = 5
# projectile settings
projectile_image_path = "FPSmin/assets/black.png"
projectile_image = load_img(projectile_image_path, gb_colorkey)
projectile_image_size = (5, 5)
projectile_speed = 20
projectile_rotation_speed = 30
projectile_life_time = 5
projectile_max_health = fps * projectile_life_time
