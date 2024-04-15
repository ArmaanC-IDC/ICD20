import pygame
from sys import exit
import random
pygame.init()

WIDTH = 1350
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("White Window")
clock = pygame.time.Clock()

background_image = pygame.image.load("unit 5/mario_game/background.jpg")
background_image = pygame.transform.scale(background_image, (1360, 750))

img1_x = 0
img2_x = 1350
game_movement = 0
game_position = 0

mario_y = HEIGHT-150
mario_speed = 0
mario_grounded = True

pipes = []
generated_pipes = [0]

def scroll_background(img1_x, img2_x, movement):
    img1_x -= movement
    img2_x -= movement

    screen.blit(background_image, (img1_x, 0))
    screen.blit(background_image, (img2_x, 0))

    if img1_x < -1350:
        img1_x = 1350
        
    if img1_x > 1350:
        img1_x = -1350

    if img2_x < -1350:
        img2_x = 1350

    if img2_x > 1350:
        img2_x = -1350
    return img1_x, img2_x

def handle_pipes():
    if game_position%500==0 and game_position not in generated_pipes:
        pipe_x = random.randint(game_position+1350, game_position+1500)
        pipe_size = random.randint(100,200)
        pipes.append([pipe_x, pipe_size, pygame.Rect(pipe_x-game_position, HEIGHT-pipe_size-150, 50, pipe_size+150)])
        generated_pipes.append(game_position)


    for i in range(len(pipes)):
        pipes[i][2]=pygame.Rect(pipes[i][0]-game_position, HEIGHT-pipes[i][1]-150, 50, pipes[i][1]+150)
        pygame.draw.rect(screen, 'GREEN', pygame.Rect(pipes[i][0]-game_position, HEIGHT-pipes[i][1]-150, 50, pipes[i][1]+150))

def handle_mario(mario_speed, mario_y):
    mario_speed +=1
    mario_y +=mario_speed
    if mario_y>=HEIGHT-160:
        mario_y = HEIGHT-160
        mario_grounded = True
    else:
        mario_grounded = False

    player_rect = pygame.Rect(90, mario_y-10, 20, 20)
    '''pygame.draw.rect(screen, 'BLACK', player_rect)'''
    pygame.draw.circle(screen, 'RED', (100, mario_y), 10)

    return mario_grounded, mario_y, mario_speed, player_rect

def collisions(game_movement, mario_y, mario_speed):
    for el in pipes:
        left_rect = pygame.Rect(el[0]-game_position, HEIGHT - el[1]-140, 1, el[1]+150)
        '''pygame.draw.rect(screen, 'BLACK', left_rect)'''
        if player_rect.colliderect(left_rect):
            print('left side')
            game_movement -= 5

        right_rect = pygame.Rect(el[0]-game_position+49, HEIGHT - el[1]-140, 1, el[1]+150)
        '''pygame.draw.rect(screen, 'BLACK', right_rect)'''
        if player_rect.colliderect(right_rect):
            print('right side')
            game_movement += 5

        '''if mario_y>=HEIGHT-el[1]-160 and (el[0]-game_position<=110 and el[0]-game_position>=90):'''
        if el[0]-game_position<=110 and el[0]-game_position>=90:
            print('true')
            mario_y = HEIGHT-el[1]-160
            mario_speed = 0


    return game_movement, mario_y, mario_speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        game_movement -= 5

    if keys[pygame.K_RIGHT]:
        game_movement += 5

    if keys[pygame.K_UP] and mario_grounded:
        mario_speed = -25

    game_movement, mario_y, mario_speed = collisions(game_movement, mario_y, mario_speed)

    img1_x, img2_x = scroll_background(img1_x, img2_x, game_movement)

    handle_pipes()

    mario_grounded, mario_y, mario_speed, player_rect = handle_mario(mario_speed, mario_y)

    game_position += game_movement 


    game_movement = 0
    pygame.display.update()
    clock.tick(60)