import pygame
from sys import exit
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_y = 10
running = True
while running:
    screen.fill('WHITE')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            exit()

    player_y +=1
    if player_y
        
    pygame.draw.circle(screen, 'GREEN', (50, player_y), 10)

    pygame.display.update()
    clock.tick(30)
    
