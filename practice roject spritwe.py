import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangular Sprites")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Rectangles (sprites)
rect1 = pygame.Rect(100, 100, 60, 60)   # movable sprite
rect2 = pygame.Rect(400, 300, 100, 80)  # static sprite

# Speed of movement
speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key controls for rect1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect1.y -= speed
    if keys[pygame.K_DOWN]:
        rect1.y += speed
    if keys[pygame.K_LEFT]:
        rect1.x -= speed
    if keys[pygame.K_RIGHT]:
        rect1.x += speed

    # Fill screen
    screen.fill(WHITE)

    # Draw sprites
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)
