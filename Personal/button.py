# Initialize Pygame
import pygame
import sys
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Button Example")

# Set up font
font = pygame.font.Font(None, 36) # none means use defalt font, 72 is the font size font size

# Define a Button class
class Button:
    def __init__(self, x, y, width, height, text): #initializes a bunch of variables
        self.rect = pygame.Rect(300,200,200,50) #creates the rectangle at (300,200) with the size of 200 by 50

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)  # screen is a variable, (0,255,0) is rgb, rect is a variable at line 17
        text_surface = font.render("Click Me", True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.centerx - text_surface.get_width() // 2, self.rect.centery - text_surface.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                print("Button Clicked")

# Create a button

button = Button(300, 200, 200, 50, "Click Me")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass events to the button
        button.handle_event(event)

    # Drawing goes here
    screen.fill((255, 255, 255))  # White background
    button.draw()

    pygame.display.flip()
