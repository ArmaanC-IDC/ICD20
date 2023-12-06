import pygame
import sys
pygame.init()

#initing variables
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

#initing variables for text input 
input_box = pygame.Rect(100, 100, 300, 50)
font = pygame.font.Font(None, 32)
user_text = ''

def get_text_input(event, text='', color=(255, 255, 255)):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            text = text[:-1]
        elif event.key==pygame.K_RETURN:
            return text
        else:
            text += event.unicode

    display_text = font.render(text, True, color)
    screen.blit(display_text, (50,50))
    return text

while True:     
    for event in pygame.event.get():
        screen.fill((255, 255, 255))
        result = get_text_input(event, text=user_text,color=(255, 0, 0))
        if result != user_text:
            user_text = result
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(user_text)
    pygame.display.update()
    clock.tick(60)