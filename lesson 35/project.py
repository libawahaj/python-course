import pygame

pygame.init()

screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game Screen')

# Colours
WHITE = (255, 255, 255)
BLUE = (0, 125, 255)
BLACK = (0, 0, 0)

rect_width, rect_height = 100, 70
rect_x = 200
rect_y = 500

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and rect_y > 0:  
        rect_y -= 2
    if keys[pygame.K_DOWN] and rect_y < screen_height - rect_height:  
        rect_y += 2
    if keys[pygame.K_LEFT] and rect_x > 0: 
        rect_x -= 2
    if keys[pygame.K_RIGHT] and rect_x < screen_width - rect_width: 
        rect_x += 2

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, pygame.Rect(200, 40, 100, 70))  
    pygame.draw.rect(screen, BLUE, pygame.Rect(rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

pygame.quit()
