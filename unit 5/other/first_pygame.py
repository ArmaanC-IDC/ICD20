import sys
# sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('I CAN MAKE THIS SAY WHATEVER I WANT')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen with white
    screen.fill((255, 255, 255))
    #redraw screen
    pygame.display.flip()

pygame.quit()