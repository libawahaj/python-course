import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((58, 58, 58))
pygame.display.set_caption('My First Game Screen')

image = pygame.image.load('image88.png') 
image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((58, 58, 58))

    screen.blit(image, image_rect)

    pygame.display.flip()
    
pygame.quit()
