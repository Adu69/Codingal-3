import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle and Text Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font setup
font = pygame.font.SysFont("Arial", 36)

# Text surface
text = font.render("Hello, Pygame!", True, BLACK)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill screen
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))  # (x, y, width, height)

    # Draw text
    screen.blit(text, (320, 220))  # place text on screen

    # Update display
    pygame.display.flip()
