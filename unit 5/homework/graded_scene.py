import math
import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

font = pygame.font.Font(None,50)


running = True
while running:
    screen.fill('LIGHTBLUE1')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

#mountains
    pygame.draw.polygon(screen,'GRAY45',[(0,800),(0,600),(150,200),(250,400),(400,250),(550,600),(800,200),(950,400),(1000,700),(1000,800)])
    pygame.draw.polygon(screen,'GRAY60',[(0,800),(0,400),(150,250),(250,450),(400,300),(550,250),(625,400),(800,250),(950,450),(1000,300),(1000,800)])
    
#green + pond at bottom
    pygame.draw.rect(screen,'GREEN4',pygame.Rect(0,600,1000,200))
    pygame.draw.ellipse(screen,'LIGHTSLATEBLUE',pygame.Rect(500,650,400,125))

#clouds
    pygame.draw.ellipse(screen,'GRAY75',pygame.Rect(100,25,300,100))
    pygame.draw.ellipse(screen,'GRAY75',pygame.Rect(125,50,250,100))

#sun
    pygame.draw.circle(screen,'YELLOW',(750,150),50)
    pygame.draw.line(screen,'YELLOW',(750,50),(750,250),10)
    pygame.draw.line(screen,'YELLOW',(650,150),(850,150),10)
    pygame.draw.line(screen,'YELLOW',(700,100),(800,200),10)
    pygame.draw.line(screen,'YELLOW',(800,100),(700,200),10)

#house
    pygame.draw.rect(screen,'BURLYWOOD4',pygame.Rect(50,500,200,200))
    pygame.draw.polygon(screen,'CORAL1',[(50,500),(250,500),(150,400)])

#text
    screen.blit(font.render('MOUNTAIN COTTAGE SCENE',True,'BLACK'),(10,10))

    pygame.display.update()