#importing the pygame module
import pygame

# Initializing Pygame
pygame.init()

# Setting the parameters for the game screen, setting width and height as 500 pixels each
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
# Setting the title of the screen
pygame.display.set_caption("My first game screen")

# setting the color of background
bg_color = pygame.Color("grey")

# Loading the image and setting the size (300x300 pixels)
image = pygame.transform.scale(
    pygame.image.load("hlelo.jpg").convert_alpha(), (300, 300)
)
#setting the position of the image to be at the center of the screen by using get_rect, which returns a rectangle object with the dimensions of the image into a variable(center) and we can 
#use it to set position of the image in the center
image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop to keep the window open and display the image
#"running" = true, so until the user closes the window, the loop will keep running
running = True
# while loop so that while the window is open, it keeps checking for events like closing the window, also keeps performing the following code
while running:
    #keeps checking for events like the user closing the window, in which case running becomes false, and breaks the loop and closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#calling upon the variables we made earlier for background color, image and image position to display them on the screen
    screen.fill(bg_color)
    screen.blit(image, image_rect)
# when we make any changes to the screen, we need to update it using pygame.display.flip(), if we dont, we simply wont be able to see any changes
    pygame.display.flip()
# quitting and cllosing pygamd
pygame.quit()
