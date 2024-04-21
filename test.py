import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define constants
GRAVITY = 0.6
JUMP_SPEED = -10
GROUND_HEIGHT = SCREEN_HEIGHT - 50

# Set up game variables
dino_size = 50
dino_x = 100
dino_y = GROUND_HEIGHT
dino_velocity = 0
dino_jumping = False

cactus_width = 30
cactus_height = 50
cactus_speed = 5
cactus_list = []

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino_jumping:
                dino_jumping = True
                dino_velocity = JUMP_SPEED

    # Update dino
    if dino_jumping:
        dino_velocity += GRAVITY
        dino_y += dino_velocity
        if dino_y >= GROUND_HEIGHT:
            dino_y = GROUND_HEIGHT
            dino_velocity = 0
            dino_jumping = False

    # Draw dino
    pygame.draw.rect(screen, BLACK, (dino_x, dino_y - dino_size, dino_size, dino_size))

    # Spawn cactus
    if random.randint(0, 100) < 2:
        cactus_list.append([SCREEN_WIDTH, GROUND_HEIGHT - cactus_height])

    # Update cactus
    for cactus in cactus_list:
        cactus[0] -= cactus_speed
        pygame.draw.rect(screen, BLACK, (cactus[0], cactus[1], cactus_width, cactus_height))

    # Remove cactus if off-screen
    cactus_list = [cactus for cactus in cactus_list if cactus[0] > -cactus_width]

    # Check collisions
    for cactus in cactus_list:
        if dino_x < cactus[0] + c
