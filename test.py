import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Countdown Timer")

# Define game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
time_remaining = 10  # Initial time in seconds

# Game loop
running = True
while running:
    screen.fill('WHITE')

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control the frame rate
    # Update game elements
    time_text = font.render(f"Time: {int(time_remaining)}", True, 'BLACK')
    screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, SCREEN_HEIGHT // 2 - time_text.get_height() // 2))

    # Decrease the time_remaining by the amount of time that has passed since the last frame
    time_remaining -= clock.get_time() / 1000  # Convert milliseconds to seconds

    # # Check if time has run out
    if time_remaining <= 0:
        time_remaining = 0
        running = False

    # Refresh screen
    pygame.display.flip()

    

# Quit Pygame
pygame.quit()
sys.exit()
