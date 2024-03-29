import pygame
import math
import random
pygame.init() 

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Moving rectangle")
clock = pygame.time.Clock()

player_x = 200
player_y = 200

PLAYER_RADIUS = 10
PLAYER_SPEED = 10

catch_count = 0
enemy_radius = 50
enemy_x,enemy_y = 20,20
pygame.draw.circle(screen,'RED',(enemy_x,enemy_y),enemy_radius)

running = True

while running:
    screen.fill('WHITE')  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
 
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and player_x>0: 
        player_x -= PLAYER_SPEED  

    if keys[pygame.K_RIGHT] and player_x<SCREEN_WIDTH-PLAYER_RADIUS: 
        player_x += PLAYER_SPEED   

    if keys[pygame.K_UP] and player_y>0: 
        player_y -= PLAYER_SPEED

    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT-PLAYER_RADIUS: 
        player_y += PLAYER_SPEED 

    pygame.draw.circle(screen, 'BLACK',(player_x,player_y),PLAYER_RADIUS)



    pygame.draw.circle(screen,'RED',(enemy_x,enemy_y),enemy_radius) 

    if abs(enemy_x-player_x)<=(PLAYER_RADIUS+enemy_radius) and abs(enemy_y-player_y)<=(PLAYER_RADIUS+enemy_radius):
        enemy_x = random.randint(0,SCREEN_WIDTH-15)
        enemy_y = random.randint(0,SCREEN_HEIGHT-15)
        catch_count+=1
        if catch_count>=2:
            enemy_radius-=1
            




    pygame.display.update()

    clock.tick(30)
pygame.quit()