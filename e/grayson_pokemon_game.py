import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Battle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
FONT = pygame.font.SysFont(None, 30)

# Player and enemy images
PLAYER_IMAGE = pygame.Surface((100, 100))
PLAYER_IMAGE.fill(GREEN)
ENEMY_IMAGE = pygame.Surface((100, 100))
ENEMY_IMAGE.fill(RED)

def display_battle_info(player_name, enemy_name, player_hp, enemy_hp):
    WIN.fill(WHITE)
    # Draw player and enemy
    WIN.blit(PLAYER_IMAGE, (50, HEIGHT // 2 - 50))
    WIN.blit(ENEMY_IMAGE, (WIDTH - 150, HEIGHT // 2 - 50))
    # Display names and HP
    player_text = FONT.render(f"{player_name}: {player_hp} HP", True, BLACK)
    enemy_text = FONT.render(f"{enemy_name}: {enemy_hp} HP", True, BLACK)
    WIN.blit(player_text, (20, 20))
    WIN.blit(enemy_text, (WIDTH - 200, 20))
    pygame.display.update()

def main():
    player_name = "Player"
    enemy_name = "Enemy"
    player_hp = 100
    enemy_hp = 100

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        display_battle_info(player_name, enemy_name, player_hp, enemy_hp)

if __name__ == "__main__":
    main()
