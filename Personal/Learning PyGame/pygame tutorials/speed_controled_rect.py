#importing and initing modules
import pygame
from sys import exit
pygame.init()

#creating the window, rectangle, and clock
width = 1250
height = 800
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
player = pygame.Rect(300,300,50,50)

#call the window rectangle game
pygame.display.set_caption("Rectangle Game")

#defining some variables
scale_factor = 20
running = True

#main game loop
while running:
    #makes the screen white
    screen.fill((255,255,255))

    #sets key to whatever keys are pressed
    key = pygame.key.get_pressed()

    #draws the rectangle on the screen
    pygame.draw.rect(screen,(0,0,0),player)

    #acceleration and deceleration
    if key[pygame.K_l]==True:
        scale_factor = scale_factor+1
    if key[pygame.K_j]==True:
        scale_factor = scale_factor-1

    #makes sure the scale never gets negative
    if scale_factor<=0:
        scale_factor = 1

    #makes the rect move
    if key[pygame.K_a]==True:
        player.move_ip(-1*scale_factor,0)
    if key[pygame.K_d]==True:
        player.move_ip(1*scale_factor,0)
    if key[pygame.K_w]==True:
        player.move_ip(0,-1*scale_factor)
    if key[pygame.K_s]==True:
        player.move_ip(0,1*scale_factor)

    #stops it from going off the screen
    if player.x<10:
        player.x = 10
    if player.x>width-10:
        player.x = width-10
    if player.y<10:
        player.y = 10
    if player.y>height-10:
        player.y = height-10

    #makes sure the game doesn't run to fast
    clock.tick(60)

    #lets you x out of the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #updates the screen
    pygame.display.update()
exit()