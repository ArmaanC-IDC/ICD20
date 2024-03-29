import pygame
from pygame.locals import *
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw 3D Shape")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_3d_shape(vertices):
    # Define edges
    edges = []
    num_vertices = len(vertices)
    for i in range(num_vertices):
        edges.append((i, (i + 1) % num_vertices))

    # Main game loop
    running = True
    while running:
        DISPLAY.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Draw edges
        for edge in edges:
            start = vertices[edge[0]]
            end = vertices[edge[1]]
            start_x, start_y, start_z = start
            end_x, end_y, end_z = end
            pygame.draw.line(DISPLAY, WHITE, (int(start_x) + WIDTH // 2, int(start_y) + HEIGHT // 2),
                             (int(end_x) + WIDTH // 2, int(end_y) + HEIGHT // 2))

        pygame.display.update()

    # Quit Pygame
    pygame.quit()

# Example usage
vertices = [(0,0,0),(100,100,100)]  # Example list of vertices
draw_3d_shape(vertices)
