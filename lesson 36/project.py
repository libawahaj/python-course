import pygame
import random

pygame.init()

COLOR_CHANGE_EVENT = pygame.USEREVENT

# colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

colors = [BLUE, DARKBLUE, YELLOW, MAGENTA, ORANGE]

screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color Changing Collision Sprites")
screen.fill(WHITE)

rect_width, rect_height = 100, 70
rect_x, rect_y = 200, 500
rect_color = DARKBLUE

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == COLOR_CHANGE_EVENT:
            rect_color = random.choice(colors)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= 1
    if keys[pygame.K_DOWN] and rect_y < screen_height - rect_height:
        rect_y += 1
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= 1
    if keys[pygame.K_RIGHT] and rect_x < screen_width - rect_width:
        rect_x += 1

    screen.fill(WHITE)

    sp1 = pygame.draw.rect(screen, LIGHTBLUE, pygame.Rect(300, 300, 100, 70))
    sp2 = pygame.draw.rect(screen, rect_color, pygame.Rect(rect_x, rect_y, rect_width, rect_height))

    if sp1.colliderect(sp2):
        pygame.event.post(pygame.event.Event(COLOR_CHANGE_EVENT))

    pygame.display.flip()

pygame.quit()
