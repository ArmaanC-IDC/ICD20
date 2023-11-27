import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRAVITY = 1
JUMP_HEIGHT = -15
PIPE_WIDTH = 50
MIN_PIPE_HEIGHT = 50
MIN_PIPE_GAP = 200
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game variables
velocity = 0
bird_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 - 10, 20, 20)  # Adjust starting position
pipes = []

def create_pipe():
    # Ensure that the pipes are generated with enough space for the bird to pass
    min_pipe_height = max(MIN_PIPE_HEIGHT, SCREEN_HEIGHT - bird_rect.height - MIN_PIPE_GAP)
    max_pipe_height = SCREEN_HEIGHT - MIN_PIPE_GAP - min_pipe_height

    # Adjust the random range if needed
    if max_pipe_height > min_pipe_height:
        pipe_height = random.randint(min_pipe_height, max_pipe_height)
    else:
        pipe_height = min_pipe_height

    upper_pipe = pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, pipe_height)
    lower_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + MIN_PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height - MIN_PIPE_GAP)
    return upper_pipe, lower_pipe

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = JUMP_HEIGHT

    # Bird movement
    velocity += GRAVITY
    bird_rect.y += velocity

    # Prevent the bird from falling below the bottom of the screen
    if bird_rect.bottom > SCREEN_HEIGHT:
        bird_rect.bottom = SCREEN_HEIGHT
    # Prevent the bird from going off the top of the screen
    if bird_rect.top < 0:
        bird_rect.top = 0

    # Create new pipes
    if random.random() < 0.02:
        pipes.extend(create_pipe())

    # Update pipes
    new_pipes = []
    for pipe in pipes:
        pipe.x -= 5  # Adjust speed as needed
        if pipe.right > 0:
            new_pipes.append(pipe)

    pipes = new_pipes

    # Check for collisions with pipes
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            pygame.quit()
            sys.exit()

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.right > 0]

    # Draw background
    screen.fill(WHITE)

    # Draw square-shaped bird
    pygame.draw.rect(screen, BLACK, bird_rect)

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, RED, pipe)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)