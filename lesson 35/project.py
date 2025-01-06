import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))

running = True 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.display.set_caption('Game screen')
        pygame.draw.rect(screen,(0,125,255), pygame.Rect(200,40,20,30))
        pygame.draw.rect(screen,(0,0,0), pygame.Rect(200,40,20,30))
        

    pygame.display.flip()
        
