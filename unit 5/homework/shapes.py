import pygame as pg
import math
pg.init()

LENGTH = 500
WIDTH = 500
screen = pg.display.set_mode((LENGTH, WIDTH))
screen.fill((100,100,100))
pg.display.set_caption('PYGAME DRAWINGS')
clock = pg.time.Clock()

def house():
    pg.draw.polygon(screen, (255,155,155),[(250,20),(150,120), (350,120)])
    pg.draw.rect(screen,(255,155,155), pg.Rect(150,120,200,200))
    pg.draw.rect(screen,(165,42,42),pg.Rect(225,220,50,100))
    pg.draw.circle(screen,(129,193,255), (250,170),30)

def tree():
    pg.draw.rect(screen,(102,51,0), pg.Rect(225,400,50,100))
    pg.draw.polygon(screen,(50,155,50), [(250,200),(100,400),(400,400)])
    pg.draw.polygon(screen,(50,155,50), [(250,100),(150,250),(350,250)])

def smiley_face():
    pg.draw.circle(screen, (255,255,0), (200, 200), 100)
    pg.draw.circle(screen, (0,0,0), (150, 170), 10)
    pg.draw.circle(screen, (0,0,0), (250, 170), 10)
    pg.draw.arc(screen, (0,0,0), (150, 180, 100, 60), math.pi, 2*math.pi, 2)

def car():
    pg.draw.rect(screen, (0,0,255), pg.Rect(50, 150, 400, 100))
    pg.draw.rect(screen, (50,50,50), pg.Rect(90, 160, 100, 50))
    pg.draw.rect(screen, (50,50,50), pg.Rect(310, 160, 100, 50))
    pg.draw.circle(screen, (0,0,0), (110, 270), 30)
    pg.draw.circle(screen, (0,0,0), (390, 270), 30)

def rocket_ship():
    pg.draw.rect(screen, (128, 128, 128), pg.Rect(200, 200, 100, 200))
    pg.draw.polygon(screen, (255, 0, 0), [(200, 200), (250, 150), (300, 200)])
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(220, 250, 20, 20))
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(260, 250, 20, 20))
    pg.draw.rect(screen, (128, 128, 128), pg.Rect(200, 400, 20, 50))
    pg.draw.rect(screen, (128, 128, 128), pg.Rect(280, 400, 20, 50))

def sun():
    pg.draw.circle(screen,(255,255,0),(250,250),100)
    pg.draw.line(screen,(255,255,0),(250,50),(250,450),10)
    pg.draw.line(screen,(255,255,0),(50,250),(450,250),10)
    pg.draw.line(screen,(255,255,0),(100,100),(400,400),10)
    pg.draw.line(screen,(255,255,0),(400,100),(100,400),10)

def snowman():
    pg.draw.circle(screen,'WHITE',(250,400),100)
    pg.draw.circle(screen,(255,255,255),(250,300),75)
    pg.draw.circle(screen,(255,255,255),(250,200),60)

    pg.draw.circle(screen,(0,0,0),(225,175),15)
    pg.draw.circle(screen,(0,0,0),(275,175),15)

    pg.draw.circle(screen,(0,0,0),(250,275),15)
    pg.draw.circle(screen,(0,0,0),(250,325),15)
    pg.draw.circle(screen,(0,0,0),(250,375),15)

    pg.draw.arc(screen,(0,0,0),pg.Rect(200,175,100,60),math.pi,2*math.pi,5)

def flagpole():
    pg.draw.line(screen,(0,0,0),(250,500),(250,100),10)
    pg.draw.polygon(screen,(255,0,0),[(250,100),(250,200),(100,150)])
    pg.draw.line(screen,(255,255,0),(100,150),(250,150),5)

running = True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running = False

    # house()
    # tree()
    # car()
    # rocket_ship()
    # sun()
    # snowman()
    flagpole()
    pg.display.flip()
    clock.tick(30)