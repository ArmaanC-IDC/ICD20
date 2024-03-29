#import and init pygame and fonts
import pygame
pygame.init()
pygame.font.init()

WIDTH = 720
HEIGHT = 1280
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # creates a screen
screen.fill('WHITE') # fills screen with color

#init a font
font = pygame.font.SysFont(None,24,False,True) #font, size, bold, italics

#create a player (use rect for colissions)
player = pygame.Surface((100,100)) #size
player_rect = player.get_rect(bottomleft = (50,50))
running = True
while running:	

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running = False
			
    #create text
	text = font.render("TEXT", True, 'RED')
	screen.blit(text, (100,100)) #text, location
	
    #
	
	pygame.display.init()
