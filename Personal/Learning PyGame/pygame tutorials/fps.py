import pygame
import sys
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple FPS Game")
clock = pygame.time.Clock()

# Player
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Update display
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.flip()
    clock.tick(FPS)
