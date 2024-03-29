#house, trees, car, sun, stick man, flag with 2 color

import pygame
import math
pygame.init()

HEIGHT = 720
WIDTH = 1280
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
pygame.display.set_caption('PYGAME DRAWINGS')
clock = pygame.time.Clock()

def house():
    pygame.draw.rect(screen,'WHEAT',pygame.Rect(WIDTH/2-100,HEIGHT-200,200,200)) #main house
    pygame.draw.polygon(screen,'WHEAT',[(WIDTH/2,HEIGHT-400),(WIDTH/2-100,HEIGHT-200),(WIDTH/2+100,HEIGHT-200)]) #roof
    pygame.draw.rect(screen,'BROWN',pygame.Rect(WIDTH/2-20,HEIGHT-100,40,100)) #door
    pygame.draw.rect(screen,'POWDERBLUE',pygame.Rect(WIDTH/2-75,HEIGHT-175,50,50)) #window left
    pygame.draw.rect(screen,'POWDERBLUE',pygame.Rect(WIDTH/2+25,HEIGHT-175,50,50)) #window right

def tree(coord):
    x = coord
    y = HEIGHT
    pygame.draw.rect(screen,'LIGHTSALMON4',pygame.Rect(x,y-100,50,100))
    pygame.draw.polygon(screen,'chartreuse4',[(x-50,y-100),(x+100,y-100),(x+25,y-400)])

def stick_man(coord):
    pygame.draw.lines(screen,'BLACK', False, [(coord,HEIGHT),(coord+25,HEIGHT-50),(coord+25,HEIGHT-100)],5)
    pygame.draw.lines(screen,'BLACK', False, [(coord+50,HEIGHT),(coord+25,HEIGHT-50)],5)
    pygame.draw.circle(screen,'BLACK', (coord+25,HEIGHT-125),25,5)
    pygame.draw.lines(screen,'BLACK', False, [(coord,HEIGHT-100),(coord+25,HEIGHT-75),(coord+50,HEIGHT-100)],5)
    pygame.draw.circle(screen,'BLACK',(coord+15,HEIGHT-130),5)
    pygame.draw.circle(screen,'BLACK',(coord+35,HEIGHT-130),5)
    pygame.draw.arc(screen,'BLACK',pygame.Rect(coord+10,HEIGHT-130,30,20),math.pi,0,3)

def sun():
    pygame.draw.circle(screen,(255,255,0),(150,150),50)
    pygame.draw.line(screen,'yellow',(150,50),(150,250),10)
    pygame.draw.line(screen,'yellow',(50,150),(250,150),10)
    pygame.draw.line(screen,'yellow',(100,100),(200,200),10)
    pygame.draw.line(screen,'yellow',(200,100),(100,200),10)

def flag(coord):
    pygame.draw.line(screen,('black'),(coord,HEIGHT),(coord,HEIGHT-600),10)
    pygame.draw.rect(screen,'magenta',pygame.Rect(coord+5,HEIGHT-600,300,100))
    pygame.draw.rect(screen,'red',pygame.Rect(coord+105,HEIGHT-600,100,100))

def car(coord):
    pygame.draw.rect(screen,'red2',pygame.Rect(coord,HEIGHT-75,200,50)) #main body
    pygame.draw.circle(screen,'black',(coord+50,HEIGHT-25),25) #left wheel
    pygame.draw.circle(screen,'white',(coord+50,HEIGHT-25),15) #left wheel inside
    pygame.draw.circle(screen,'black',(coord+150,HEIGHT-25),25) #right wheel
    pygame.draw.circle(screen,'white',(coord+150,HEIGHT-25),15) #right wheel inside
    pygame.draw.polygon(screen,'red2',[(coord+100,HEIGHT-75),(coord+100,HEIGHT-125),(coord+175,HEIGHT-125),(coord+200,HEIGHT-75)])
    pygame.draw.polygon(screen,'skyblue',[(coord+165,HEIGHT-115),(coord+190,HEIGHT-75),(coord+165,HEIGHT-75)])

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    house()
    tree(75)
    tree(250)
    sun()
    stick_man(400)
    flag(800)
    car(900)
    pygame.draw.arc(screen,'BLACK',pygame.Rect(500,0,200,200),math.pi/180*160,math.pi,100)
    pygame.display.flip()
    clock.tick(30)