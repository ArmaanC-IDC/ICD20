import pygame
from pygame.locals import *
import cv2
import numpy as np

# Initialize Pygame
pygame.init()

# Set up Pygame window
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 450  # 16:9 aspect ratio
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Face Detection')

# Initialize the camera and face detector
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Capture frame from camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize frame to fit the Pygame window while maintaining aspect ratio
    aspect_ratio = frame.shape[1] / frame.shape[0]
    target_width = int(WINDOW_HEIGHT * aspect_ratio)
    if target_width > WINDOW_WIDTH:
        target_width = WINDOW_WIDTH
        target_height = int(WINDOW_WIDTH / aspect_ratio)
    else:
        target_height = WINDOW_HEIGHT
    frame = cv2.resize(frame, (target_width, target_height))

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Calculate the position to center the frame in the Pygame window
    x_offset = (WINDOW_WIDTH - target_width) // 2
    y_offset = (WINDOW_HEIGHT - target_height) // 2

    # Convert frame to Pygame surface
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    frame_surface = pygame.surfarray.make_surface(cv2.flip(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), 1))

    # Display the frame
    window.blit(frame_surface, (x_offset, y_offset))
    pygame.display.flip()

    # Check for quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

# Release the camera and close Pygame window
cap.release()
pygame.quit()