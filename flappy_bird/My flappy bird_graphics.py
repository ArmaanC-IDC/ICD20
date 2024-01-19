def main():
    import pygame
    from sys import exit
    from random import randint
    pygame.init()

    screen = pygame.display.set_mode((800, 500))
    clock = pygame.time.Clock()

    pipe_low1 = pygame.image.load("flappy_bird/low_pipe.png")
    pipe_low_rect1 = pipe_low1.get_rect(topright = (0, 400))

    pipe_top1 = pygame.Surface((50,400))
    pipe_top1.fill((55,255,55))
    pipe_top_rect1 = pipe_top1.get_rect(bottomright = ((0, 0)))

    height = randint(200,300)

    pipe_low2 = pygame.image.load("flappy_bird/low_pipe.png")
    pipe_low_rect2 = pipe_low2.get_rect(topright = (1400, height))

    pipe_top2 = pygame.Surface((50,400))
    pipe_top2.fill((55,255,55))
    pipe_top_rect2 = pipe_top2.get_rect(bottomright = ((1400, height-200)))

    player = pygame.image.load("flappy_bird/bird_wings_down.png")
    player_rect = player.get_rect(bottomleft = (50,50))

    font = pygame.font.Font(None, 50)

    yes_button = pygame.Surface((100,50))
    yes_button.fill((0,255,0))
    yes_buton_rect = yes_button.get_rect(midbottom = (250, 250))

    no_button = pygame.Surface((100,50))
    no_button.fill((255,0,0))
    no_buton_rect = no_button.get_rect(midbottom = (750, 250))

    score = 0
    score_text = font.render(str(score), True, (0,0,0))
    score_rect = score_text.get_rect(midbottom = (500, 250))

    scale_factor = 10
    velocity = 0
    game_on = True
    while True:
        if game_on==True:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        velocity = -15*((scale_factor-3)/7)
                
            velocity += (scale_factor-7)/3
            player_rect.y += velocity
            if player_rect.y>450: 
                velocity = 0
                player_rect.y = 450
            elif player_rect.y <=10:
                player_rect.y = 10
                velocity = 0
            screen.blit(player, player_rect)

            #recycles them when they get to the end
            if pipe_low_rect1.x<-50: 
                height = randint(250,450)
                pipe_low_rect1.x = 850
                pipe_low_rect1.y = height
                pipe_top_rect1.y = height-600
                score += 1
            #makes them move
            pipe_low_rect1.x -= 1*scale_factor
            pipe_top_rect1.x = pipe_low_rect1.x

            #recycles them when they get to the end
            if pipe_low_rect2.x<-50: 
                height2 = randint(250,450)
                pipe_low_rect2.x = 850
                pipe_low_rect2.y = height2
                pipe_top_rect2.y = height2-600
                scale_factor+=0.5
                score += 1
            #makes them move
            pipe_low_rect2.x -= 1*scale_factor
            pipe_top_rect2.x = pipe_low_rect2.x

            #check for collisions
            if player_rect.colliderect(pipe_top_rect1) or player_rect.colliderect(pipe_top_rect2) or player_rect.colliderect(pipe_low_rect1) or player_rect.colliderect(pipe_low_rect2):
                game_on = False

            score_text = font.render(str(score), True, (0,0,0))
            score_rect = score_text.get_rect(topright = (950, 50))
                
            screen.blit(pipe_low2, pipe_low_rect2)
            screen.blit(pipe_top2, pipe_top_rect2)
            screen.blit(pipe_low1, pipe_low_rect1)
            screen.blit(pipe_top1, pipe_top_rect1)
            screen.blit(score_text, score_rect)
        else:
            screen.fill((255,255,255))
            score_text = font.render(f" Your score was {str(score)}", True, (0,0,0))
            score_rect = score_text.get_rect(midtop = (500, 50))

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if yes_buton_rect.collidepoint(mouse_pos):
                if mouse_pressed[0]:
                    score = 0
                    scale_factor = 10
                    pipe_low_rect1.x = 1000
                    pipe_top_rect1.x =  1000
                    pipe_low_rect2.x = 1500
                    pipe_top_rect2.x = 1500
                    player_rect.bottomleft = (50, 50)
                    game_on = True
                
            if no_buton_rect.collidepoint(mouse_pos):
                if mouse_pressed[0]:
                    exit()

            screen.blit(score_text, score_rect)
            screen.blit(yes_button, yes_buton_rect)
            screen.blit(no_button, no_buton_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

        pygame.display.update()
        clock.tick(30)   

main() 