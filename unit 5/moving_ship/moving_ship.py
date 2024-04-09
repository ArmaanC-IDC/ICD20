import pygame
import math
pygame.init()
WIDTH,HEIGHT = 1000,700
screen = pygame.display.set_mode((WIDTH,HEIGHT))

image = pygame.image.load("grayson_asteroids/Spaceship.png")
image = pygame.transform.scale(image,(10,10))
print(math.degrees(math.atan(45)))

def calculate_movement(angle, speed):
    delta_x = math.cos(math.radians(90 - angle))*speed
    delta_y = math.sin(math.radians(90 - angle))*speed
    
    return delta_x, delta_y



#0 is up, goes counter-clockwise
angle = 0
x = 500
y = 350
running = True
while running:
    screen.fill('RED')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        angle +=10
    if keys[pygame.K_d]:
        angle -=10
    if keys[pygame.K_s]:
        num = calculate_movement(angle,10)
        x+=num[0]
        y+=num[1]
    if keys[pygame.K_w]:
        num = calculate_movement(angle,10)
        x-=num[0]
        y-=num[1]


    
    image2 = pygame.transform.rotate(image, angle)
    screen.blit(image2, (x,y))
    pygame.display.update()
    pygame.time.Clock().tick(30)