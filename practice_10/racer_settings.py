import pygame

pygame.mixer.init()
# basic sizes
screen_width = 600
screen_height = 900

car_width = 90
car_height = 164

player_speed = 10
enemy_speed = 10

coin_width = 50
coin_height = 50
coin_speed = 3

# resources
bg = pygame.image.load("sprites/road.png")
crash_sound = pygame.mixer.Sound("sprites/dragon-studio-car-crash-sound-376882.mp3")