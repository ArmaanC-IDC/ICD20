import random
import sys
import pygame
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()
ouch = pygame.mixer.Sound('beep.wav')

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle Catcher")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
score = 0
time_remaining = 60
player_radius = 5
player_color = BLUE
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5
game_over = False
circles = []

# Function to create new circles
def create_circle():
    circles.clear()  # Clear existing circles
    radius = random.randint(5, 20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = random.randint(0, SCREEN_WIDTH - 2*radius)
    y = random.randint(0, SCREEN_HEIGHT - 2*radius)
    circle = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius}
    circles.append(circle)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game elements
    time_text = font.render(f"Time: {int(time_remaining)}", True, BLACK)
    screen.blit(time_text, (SCREEN_WIDTH - 150, 10))
     # Control the frame rate
    clock.tick(60)  # Set the frame rate to 60 frames per second
    
    if time_remaining > 0:
        # Decrease the time_remaining by the amount of time that has passed since the last frame
        time_remaining -= clock.get_time() / 1000  # Convert milliseconds to seconds
        if not circles:  # Only create a new circle if there's none on the screen
            create_circle()
    else:
          # Display score
            gamesover_text = font.render("Game Over", True, BLACK)
            text_rect = gamesover_text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(gamesover_text, text_rect)
            game_over = True

    # Draw game elements
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['rect'].center, circle['radius'])

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Move player circle with keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        player_x = max(player_x, player_radius)  # Ensure player does not move off the left edge
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        player_x = min(player_x, SCREEN_WIDTH - player_radius)  # Ensure player does not move off the right edge
    if keys[pygame.K_UP]:
        player_y -= player_speed
        player_y = max(player_y, player_radius)  # Ensure player does not move off the top edge
    if keys[pygame.K_DOWN]:
        player_y += player_speed
        player_y = min(player_y, SCREEN_HEIGHT - player_radius)  # Ensure player does not move off the bottom edge

    # Draw player circle
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    # Check for collisions between player and circles
    if game_over == False:
        player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, 2 * player_radius, 2 * player_radius)
        for circle in circles:
            if player_rect.colliderect(circle['rect']):
                score += 1
                circles.remove(circle)
                pygame.mixer.Sound.play(ouch)

    # Refresh screen
    pygame.display.flip()


pygame.quit()
sys.exit()
