import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
import time

player = pygame.Rect(300,250,50,50)
game_running = True
while game_running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    if key[pygame.K_d] == True:
        player.move_ip(1,0)
    if key[pygame.K_s] == True:
        player.move_ip(0,1)
    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False


    pygame.display.update()