import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)  # Dull Green
BLUE = (173, 216, 230)  # Light Blue

# Tower class
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.range = 100  # Tower shooting range

    def shoot(self, target):
        # Create a bullet towards the target
        dx = target.rect.centerx - self.rect.centerx
        dy = target.rect.centery - self.rect.centery
        distance = max(1, (dx**2 + dy**2)**0.5)
        
        if distance > 0:
            bullet_speed = 5
            bullet_dx = bullet_speed * dx / distance
            bullet_dy = bullet_speed * dy / distance

            bullet = Bullet(self.rect.centerx, self.rect.centery, bullet_dx, bullet_dy)
            all_sprites.add(bullet)
            bullets.add(bullet)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.max_health = random.randint(10, 20)
        self.health = self.max_health
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = path[0]
        self.path = path[1:]
        self.speed = random.randint(1, 3)
        self.update_color()

    def update_color(self):
        # Calculate the color based on health
        red = int(255 * (self.health / self.max_health))
        green = int(255 * (1 - self.health / self.max_health))
        
        # Set the color of the enemy surface
        self.image.fill((red, green, 0, 255))




    def update(self):
        if self.path:
            target_x, target_y = self.path[0]

            # Check if the enemy is close to the target
            dx = target_x - self.rect.x
            dy = target_y - self.rect.y
            distance = max(1, (dx**2 + dy**2)**0.5)

            if distance < self.speed:
                self.rect.x, self.rect.y = self.path.pop(0)
            else:
                if distance > 0:
                    normalized_direction = pygame.math.Vector2(dx, dy).normalize()
                    speed_x = self.speed * normalized_direction.x
                    speed_y = self.speed * normalized_direction.y
                    self.rect.x += speed_x
                    self.rect.y += speed_y
        else:
            # If enemy reaches the end, remove it
            enemies.remove(self)
            all_sprites.remove(self)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            enemies.remove(self)
            all_sprites.remove(self)
        self.update_color()

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check for collisions with enemies
        hit_enemies = pygame.sprite.spritecollide(self, enemies, False)  # Changed to False
        for enemy in hit_enemies:
            enemy.health -= 1
            if enemy.health <= 0:
                enemies.remove(enemy)
                all_sprites.remove(enemy)

# Difficulty class
class DifficultyButton(pygame.sprite.Sprite):
    def __init__(self, x, y, difficulty, color, font):
        super().__init__()
        self.difficulty = difficulty
        self.image = pygame.Surface((150, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.text = font.render(difficulty, True, WHITE)
        self.text_rect = self.text.get_rect(center=self.rect.center)

# Start button class
class StartButton(pygame.sprite.Sprite):
    def __init__(self, x, y, font):
        super().__init__()
        self.image = pygame.Surface((150, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.text = font.render("Start", True, WHITE)
        self.text_rect = self.text.get_rect(center=self.rect.center)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Font setup
font = pygame.font.Font(None, 36)

# Create sprite groups
all_sprites = pygame.sprite.Group()
towers = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
buttons = pygame.sprite.Group()

# Game states
GAME = "game"
state = "intro"

# Path for enemies
PATH = [(0, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT - 30)]
last_shot_time = 0

# Intro loop
while state == "intro":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = "quit"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if start_button.rect.collidepoint(x, y):
                    state = GAME

    # Draw everything
    screen.fill(WHITE)

    # Draw path for enemies
    pygame.draw.lines(screen, GREEN, False, PATH, 30)

    # Draw start button
    start_button = StartButton(WIDTH // 2, HEIGHT - 100, font)
    buttons.add(start_button)
    all_sprites.add(start_button)

    buttons.draw(screen)

    # Draw text on start button
    screen.blit(start_button.text, start_button.text_rect)

    # Display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Game loop
while state == GAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = "quit"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if start_button.rect.collidepoint(x, y):
                    state = GAME
                else:
                    tower = Tower(x, y)
                    all_sprites.add(tower)
                    towers.add(tower)
                    last_shot_time = pygame.time.get_ticks()

    # Draw everything
    screen.fill(WHITE)

    # Draw path for enemies
    pygame.draw.lines(screen, GREEN, False, PATH, 30)

    # Spawn enemies
    if random.randint(1, 100) < 2:
        enemy = Enemy(PATH.copy())
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Tower shooting
    # Tower shooting
    current_time = pygame.time.get_ticks()
    if current_time - last_shot_time > 1000 / 3:  # Fire 3 bullets per second
        for tower in towers:
            for enemy in enemies:
                distance = pygame.math.Vector2(tower.rect.center).distance_to(pygame.math.Vector2(enemy.rect.center))
                if distance < tower.range:
                    bullet_dx = (enemy.rect.centerx - tower.rect.centerx) / distance
                    bullet_dy = (enemy.rect.centery - tower.rect.centery) / distance
                    bullet = Bullet(tower.rect.centerx, tower.rect.centery, bullet_dx * 5, bullet_dy * 5)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
        last_shot_time = current_time


    # Update sprites
    all_sprites.update()

    # Draw everything
    all_sprites.draw(screen)

    # Display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)


pygame.quit()
sys.exit()
