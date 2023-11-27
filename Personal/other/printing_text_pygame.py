# Initialize Pygame (copy this every time)
import pygame
pygame.init()

# Set up display (copy this every time, change the width and height)
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Text Example")

# Set up font
font = pygame.font.Font(None, 72)  # none means use defalt font, 72 is the font size font size

# Create a text surface
text_surface = font.render('hi', True, (0,255,255),(0,0,0))  #hi is the message, true means smooth edges, (0,255,255) is rgb color code for the text, (0,0,0) is rgb for highlight

# Get the position to center the text on the screen
text_x = width // 2 - text_surface.get_width() // 2 
text_y = height // 2 - text_surface.get_height() // 2

# Main game loop (need a never-ending while True loop)
while True:
    #this lets you close the window without an error
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Drawing goes here
    screen.fill((255, 255, 255))  # fills the screen with white
    screen.blit(text_surface, (text_x, text_y)) #blitting means drawing, text_x and text_y are the coordinates of the text. 0,0 is top right

    pygame.display.flip() #updates the screen, and makes it actually do stuff