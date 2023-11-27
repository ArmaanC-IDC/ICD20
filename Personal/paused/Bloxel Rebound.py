import pygame
from sys import exit
from random import randint
pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player = pygame.Surface((50, 50))
player.fill((0,0,0))
player_rect = player.get_rect(bottomleft = (50, 650))

block1 = pygame.Surface((100000))
block1.fill((255,100,255))
block_rect1 = block1.get_rect(topleft = (-50,650))