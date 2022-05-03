import pygame
from utils.utils import *

pygame.init()
font = pygame.font.Font(None, 20)


fps = 60
width = 800
height = 800
pygame.display.set_mode((width, height))  # make it can load image
background_color = (100, 100, 200)
gb_colorkey = (1, 1, 1)
# player settings
player_image_path_green = "FPSmin/assets/green.png"
player_image_green = load_img(player_image_path_green, gb_colorkey)
player_image_path_red = "FPSmin/assets/red.png"
player_image_red = load_img(player_image_path_red, gb_colorkey)
player_image_size = (100, 100)
player_normal_speed = 7
player_slow_speed = 3
player_rotation_speed = 5

cursor_size = (8, 8)
cursor_color = (255, 255, 255)
# projectile settings
projectile_image_path = "FPSmin/assets/black.png"
projectile_image = load_img(projectile_image_path, gb_colorkey)
projectile_image_size = (10, 10)
projectile_speed = 20
projectile_rotation_speed = 30
projectile_life_time = 5
projectile_max_health = fps * projectile_life_time
