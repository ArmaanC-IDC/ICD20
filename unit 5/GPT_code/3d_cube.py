import pygame
from pygame.locals import *
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic 3D Game - Cube Rotation")
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define cube vertices
vertices = [(-1, -1, -2), (1, -1, -2), (1, 1, -2), (-1, 1, -2),
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]

# Define edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Define rotation functions
def rotate_x(vertex, angle):
    x, y, z = vertex
    rad = math.radians(angle)
    return x, y * math.cos(rad) - z * math.sin(rad), y * math.sin(rad) + z * math.cos(rad)

def rotate_y(vertex, angle):
    x, y, z = vertex
    rad = math.radians(angle)
    return x * math.cos(rad) + z * math.sin(rad), y, -x * math.sin(rad) + z * math.cos(rad)

def rotate_z(vertex, angle):
    x, y, z = vertex
    rad = math.radians(angle)
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad), z

# Main game loop
running = True
angle_x, angle_y, angle_z = 0, 0, 0
while running:
    DISPLAY.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Rotate cube based on key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle_y -= 1
    if keys[pygame.K_RIGHT]:
        angle_y += 1
    if keys[pygame.K_UP]:
        angle_x -= 1
    if keys[pygame.K_DOWN]:
        angle_x += 1

    # Apply rotation to cube vertices
    rotated_vertices = []
    for vertex in vertices:
        vertex = rotate_x(vertex, angle_x)
        vertex = rotate_y(vertex, angle_y)
        vertex = rotate_z(vertex, angle_z)
        rotated_vertices.append(vertex)

    # Draw edges
    for edge in edges:
        start = rotated_vertices[edge[0]]
        end = rotated_vertices[edge[1]]
        start_x, start_y, start_z = start
        end_x, end_y, end_z = end
        pygame.draw.line(DISPLAY, WHITE, (int(start_x * 100) + WIDTH // 2, int(start_y * 100) + HEIGHT // 2),
                         (int(end_x * 100) + WIDTH // 2, int(end_y * 100) + HEIGHT // 2))

    pygame.display.update()
    clock.tick(30)

# Quit Pygame
pygame.quit()
