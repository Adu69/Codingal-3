import pygame

pygame.init()
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window")
back_img = pygame.transform.scale(
    pygame.image.load("back.png").convert()
    , (screen_width, screen_height))

penguin_img = pygame.transform.scale(
pygame.image.load("hello penguin.png").convert_alpha(), (200, 200))
penguin_rect = penguin_img.get_rect(center=(screen_width // 2, screen_height // 2 - 30 ))

text = pygame.font.Font(None, 36).render("Hello, World!", True,pygame.Color("blue"))
text_rect = text.get_rect(center=(screen_width // 2, screen_height //2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(back_img, (0, 0))
        screen.blit(penguin_img, penguin_rect)
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()