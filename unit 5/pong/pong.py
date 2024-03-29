import pygame
import random
pygame.init()
pygame.mixer.init()

#game constants
WIDTH = 1120
HEIGHT = 500
X_SPEED_RANGE = 10,15
Y_SPEED_RANGE = 10,15
END_SCORE = 10

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PONG')
clock = pygame.time.Clock()
font = pygame.font.Font(None,30)

beep = pygame.mixer.Sound('unit 5/pong/beep.wav')
lose_point = pygame.mixer.Sound('unit 5/pong/lose_point.wav')
pygame.mixer.music.load('unit 5/pong/background_music.mp3')
pygame.mixer.music.set_volume(0.2)

#init variables
p1 = {'score':0, 'paddle_location': 250}
p2 = {'score':0, 'paddle_location': 250}

X_SPEED_LIST = [i for i in range(X_SPEED_RANGE[0],X_SPEED_RANGE[1]+1)] + [-1*i for i in range(X_SPEED_RANGE[0],X_SPEED_RANGE[1]+1)]
Y_SPEED_LIST = [i for i in range(Y_SPEED_RANGE[0],Y_SPEED_RANGE[1]+1)] + [-1*i for i in range(Y_SPEED_RANGE[0],Y_SPEED_RANGE[1]+1)]
ball = {'x': 500, 'y': 250, 'x_speed': random.choice(X_SPEED_LIST), 'y_speed': random.choice(Y_SPEED_LIST)}

pygame.mixer.music.play(-1)
running = True
game_state = 'game'
while running:
    screen.fill('WHITE')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
    if game_state=='game':

        keys = pygame.key.get_pressed()
        #p1 code
        if keys[pygame.K_w] and p1['paddle_location']>0:
            p1['paddle_location']-=30
        if keys[pygame.K_s] and p1['paddle_location']<=HEIGHT-100:
            p1['paddle_location']+=30
        pygame.draw.rect(screen,'BLACK',pygame.Rect(25,p1['paddle_location'],25,100))



        #p2 code
        if keys[pygame.K_UP] and p2['paddle_location']>0:
            p2['paddle_location']-=20
        if keys[pygame.K_DOWN] and p2['paddle_location']<=HEIGHT-100:
            p2['paddle_location']+=20

        pygame.draw.rect(screen,'BLACK',pygame.Rect(WIDTH-75,p2['paddle_location'],25,100))

        #ball code
        #check for paddle collisions
        p1_rect = pygame.Rect(25,p1['paddle_location'],25,100)
        p2_rect = pygame.Rect(WIDTH-75,p2['paddle_location'],25,100)
        ball_rect = pygame.Rect(ball['x']-10,ball['y']-10,20,20)

        if p1_rect.colliderect(ball_rect):
            ball['x_speed']=abs(ball['x_speed'])
            pygame.mixer.Sound.play(beep)
        if p2_rect.colliderect(ball_rect):
            ball['x_speed']=abs(ball['x_speed'])*-1
            pygame.mixer.Sound.play(beep)

        #check for collisions with wall
        if ball['y']<=10:
            ball['y_speed']=abs(ball['y_speed'])

        elif ball['y']>=HEIGHT-10:
            ball['y_speed']=abs(ball['y_speed'])*-1

        if ball['x']<=10:
            ball['x']=WIDTH/2
            ball['y']=HEIGHT/2
            ball['x_speed']=random.choice(X_SPEED_LIST)
            ball['y_speed']=random.choice(Y_SPEED_LIST)
            p1['score']+=1
            pygame.mixer.Sound.play(lose_point)

        elif ball['x']>=WIDTH-10:
            ball['x']=WIDTH/2
            ball['y']=HEIGHT/2
            ball['x_speed']=random.choice(X_SPEED_LIST)
            ball['y_speed']=random.choice(Y_SPEED_LIST)
            p2['score']+=1
            pygame.mixer.Sound.play(lose_point)

        #make the ball move
        ball['x'] +=ball['x_speed']
        ball['y'] +=ball['y_speed']


        pygame.draw.circle(screen,'BLACK',(ball['x'],ball['y']), 10)




        #display text
        p1_score_text = font.render(str(p1['score']),True,'BLACK')
        screen.blit(p1_score_text, (WIDTH-75,25))

        p2_score_text = font.render(str(p2['score']),True,'BLACK')
        screen.blit(p2_score_text, (25,25))

        #check for endgame
        if p1['score']>=END_SCORE:
            game_state='endgame'
        if p2['score']>=END_SCORE:
            game_state='endgame'

    elif game_state=='endgame':

        text = 'the score was ' + str(p1['score']) + ' - ' + str(p2['score'])
        endgame_score_text = font.render(text,True,'BLACK')
        screen.blit(endgame_score_text, (WIDTH//2-100, HEIGHT//2-100))
    clock.tick(30)
    pygame.display.update()

