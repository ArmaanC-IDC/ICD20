import pygame
pygame.init()
WIDTH = 800 #whatever width
HEIGHT = 600 #whatever height
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #need 2 brackets, not one
pygame.display.set_caption('whatever you want the title to be')
screen.fill((230,255,255)) #255,255,255 is RGB color code. 2 brackets is important. 255 is biggest number

running = True
while running:
    for event in pygame.event.get(): #put any logic based on events like mouse movements in this loop
        if event.type == pygame.QUIT: #this lets you close the window
            running = False
    pygame.display.flip() #always put this at the end of your while loop. it updates the screen
    