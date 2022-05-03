import pygame
from utils.utils import *

pygame.init()
font = pygame.font.Font(None, 20)

fps = 60
width = 800
height = 800
background_color = (100, 100, 200)
# player settings
player_speed = 7
player_slow_speed = 3
player_rotation_speed = 5

cursor_size = (8, 8)
cursor_color = (255, 255, 255)
# projectile settings
projectile_image_path = "FPSmin/assets/black.png"

projectile_speed = 20
projectile_rotation_speed = 30
projectile_life_time = 5
projectile_max_health = fps * projectile_life_time
