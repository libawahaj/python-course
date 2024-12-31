import pygame

pygame.init()

width, height = 600, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Adding image and background image.")

background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (width, height))

image = pygame.transform.scale(
    pygame.image.load('hello_penguin.png').convert_alpha(), (200, 200))

penguin_rect = image.get_rect(center=(width // 2, height // 2 - 30))

text = pygame.font.Font(None, 36).render("Hello World", True, pygame.Color('black'))

text_rect = text.get_rect(center=(width // 2, height // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))
        screen.blit(image, penguin_rect)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
