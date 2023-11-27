import pygame
from sys import exit
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

lazer = pygame.Surface((50, 200))
lazer.fill((255,0,0))
lazer_rect = lazer.get_rect(bottomright = (1000,500))

player = pygame.Surface((50,50))
player.fill((0,0,0))
player_rect = player.get_rect(topleft = (50, 400))

while True:
    screen.fill((255,255,255))

    lazer_rect.x -= 5
    if lazer_rect.x<-50: lazer_rect.x = width
    screen.blit(lazer, lazer_rect)

    screen.blit(player,player_rect)

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if player_rect.colliderect(lazer_rect):
         screen.fill((255,0,0))
    elif player_rect.collidepoint(mouse_pos):
        if mouse_pressed[0]:
            screen.fill((0,0,255))
            
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
               exit()
    pygame.display.update()
    clock.tick(30)