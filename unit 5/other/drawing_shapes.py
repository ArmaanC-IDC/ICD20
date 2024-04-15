# Import and initialize the pygame library
import sys
import pygame
import math

pygame.init()
WIDTH = 1280
HEIGHT = 720
# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, 720])

# Run until the user asks to quit
running = True
x = 100
x_vel = 1
box_width = 50
radius = 30
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500, 100, 50, 50)) 
    #screen is the display, rgb color, pygame.Rect(x,y coordinates, width, height)

    pygame.draw.circle(screen, (0, 255, 0), (x, 300), 100, 5)
    #display name, (rgb), (center coords), radius

    # pygame.draw.line(screen, (0, 0, 255), (0, 0), (800, 600), 20)
    #display, (rgb), start coords, seccond coords, something, thickness

    # pygame.draw.polygon(screen, (255, 255, 0), [(200, 200), (300, 300), (400, 200)])
    #display, color, verticies (all the points. this one is 3 so triangle)

    # pygame.draw.arc(screen, (255, 0, 255), pygame.Rect(10,10,500,500), 0, math.pi*1.5, 2)
    #display, color, arc goes in a rectangle pygame.Rect(coords), start(angle radians), end(angle radiens), thickness
    #circle is 2 pi radians

    # pygame.draw.ellipse(screen, (0, 0, 255), pygame.Rect(200, 200, 200, 100))
    # pygame.draw.aaline(screen, (255, 0, 255), (0, 0), (800, 600))
    # pygame.draw.lines(screen, (100, 255, 0), False, [(100, 100), (200, 200), (300, 100)], 2)
    pygame.display.update()
pygame.quit()