import pygame
import sys
import random

pygame.init()

width, height = 300, 300  # Larger screen
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake = [(150, 150)]
snake_dir = (1, 0)  # Constant movement to the right
snake_speed = 10

food = (random.randint(10, width - 10), random.randint(10, height - 10))
score = 0
level = 1

font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    win.blit(text_surface, (x, y))

def game_over():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        win.fill((255, 255, 255))  # White background
        draw_text("Game Over", width // 2 - 100, height // 2 - 50, (255, 0, 0))
        draw_text(f"Score: {score}", width // 2 - 50, height // 2, (0, 255, 0))  # Green score text
        draw_text("Press ESC to exit", width // 2 - 120, height // 2 + 50, (0, 0, 255))  # Blue exit text

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Arrow key input to change direction
    if keys[pygame.K_UP]:
        snake_dir = (0, -1)
    elif keys[pygame.K_DOWN]:
        snake_dir = (0, 1)
    elif keys[pygame.K_LEFT]:
        snake_dir = (-1, 0)
    elif keys[pygame.K_RIGHT]:
        snake_dir = (1, 0)

    # Continuous movement
    snake_head = (snake[0][0] + snake_dir[0] * 10, snake[0][1] + snake_dir[1] * 10)
    snake = [snake_head] + snake[:-1]

    # Check for collision with food
    if snake_head[0] < food[0] + 10 and snake_head[0] + 10 > food[0] and snake_head[1] < food[1] + 10 and snake_head[1] + 10 > food[1]:
        food = (random.randint(0, width - 10), random.randint(0, height - 10))
        snake.append((0, 0))
        score += 1

        if score % 5 == 0:
            snake_speed += 1
            level += 1

    # Check for collision with walls
    if snake_head[0] < 0 or snake_head[0] >= width or snake_head[1] < 0 or snake_head[1] >= height:
        game_over()

    # Check for collision with itself
    if snake_head in snake[1:]:
        game_over()

    win.fill((255, 255, 255))  # White background

    # Draw the snake in green
    for segment in snake:
        pygame.draw.rect(win, (0, 255, 0), (segment[0], segment[1], 10, 10))

    pygame.draw.rect(win, (255, 0, 0), (food[0], food[1], 10, 10))

    draw_text(f"Score: {score}", 10, 10, (0, 0, 0))  # Black score text
    draw_text(f"Level: {level}", width - 120, 10, (0, 0, 0))  # Black level text

    pygame.display.flip()

    pygame.time.Clock().tick(snake_speed)