import pygame
import random

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
FPS = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tetris shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [1]],  # J
    [[1, 1, 1], [0, 0, 1]],  # L
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1]],  # S
    [[1, 1, 1], [1, 0]],  # T
    [[1, 1], [0, 1, 1]],  # Z
]

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pygame Tetris")
        self.clock = pygame.time.Clock()

        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.spawn_piece()
        self.score = 0

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = self.grid[y][x]
                pygame.draw.rect(self.screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(self.screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def draw_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, value in enumerate(row):
                if value:
                    color = self.get_color(value)
                    pygame.draw.rect(self.screen, color, ((self.current_x + x) * GRID_SIZE, (self.current_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(self.screen, BLACK, ((self.current_x + x) * GRID_SIZE, (self.current_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def get_color(self, value):
        colors = [BLACK, CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]
        return colors[value]

    def spawn_piece(self):
        shape = random.choice(SHAPES)
        return shape

    def check_collision(self):
        for y, row in enumerate(self.current_piece):
            for x, value in enumerate(row):
                if value and (
                    self.current_x + x < 0
                    or self.current_x + x >= GRID_WIDTH
                    or self.current_y + y >= GRID_HEIGHT
                    or (self.current_y + y >= 0 and self.grid[self.current_y + y][self.current_x + x] != 0)
                ):
                    return True
        return False

    def place_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, value in enumerate(row):
                if value:
                    self.grid[self.current_y + y][self.current_x + x] = value

    def check_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if 0 not in row]
        for line in lines_to_clear:
            del self.grid[line]
            self.grid.insert(0, [0] * GRID_WIDTH)
            self.score += 1

    def run(self):
        self.current_x = GRID_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_x -= 1
                        if self.check_collision():
                            self.current_x += 1
                    elif event.key == pygame.K_RIGHT:
                        self.current_x += 1
                        if self.check_collision():
                            self.current_x -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_y += 1
                        if self.check_collision():
                            self.current_y -= 1
                    elif event.key == pygame.K_UP:
                        rotated_piece = list(zip(*reversed(self.current_piece)))
                        if self.current_x + len(rotated_piece[0]) <= GRID_WIDTH and not self.check_collision():
                            self.current_piece = rotated_piece

            self.current_y += 1
            if self.check_collision():
                self.current_y -= 1
                self.place_piece()
                self.check_lines()
                self.current_piece = self.spawn_piece()
                self.current_x = GRID_WIDTH // 2 - len(self.current_piece[0]) // 2
                self.current_y = 0

                if self.check_collision():
                    # Game over if a new piece cannot be placed
                    pygame.quit()
                    quit()

            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_piece()

            pygame.display.update()
            self.clock.tick(FPS)



if __name__ == "__main__":
    tetris_game = Tetris()
    tetris_game.run()
