import pygame
pygame.init()
pygame.font.init()

HEIGHT = 720
WIDTH = 1280
screen = pygame.display.set_mode((WIDTH,HEIGHT))

font1 = pygame.font.SysFont(None,24,)
font2 = pygame.font.SysFont(None,48,True,False)

running = True
while running:
    screen.fill('WHITE')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    text = font1.render(f"Hello World! Size 24",True,'RED','BLACK')
    screen.blit(text,(25,25))

    text2 = font2.render(f"Hello World! Size 48 bolded!",True,'RED')
    text2_rect = text2.get_rect()
    text2_rect.center = (WIDTH//2,HEIGHT//2)
    screen.blit(text2,text2_rect)

    pygame.display.update()