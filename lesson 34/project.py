import pygame

pygame.init()

#screen
screen_width = 640
screen_height = 480 

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((255,255,255))

#rectangle
rect_width = 100
rect_height = 50
left = (screen_width - rect_width) //2
top = (screen_height - rect_height) //2

#text
text_font = pygame.font.SysFont('Arial', 30)

def draw_text(text,font,colour,x,y):
    img = font.render(text,True,colour)
    screen.blit(img, (x,y))

#loop
running = True 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.display.set_caption('My first game screen')
        pygame.draw.rect(screen,(0,125,255), pygame.Rect(left, top, rect_width, rect_height))
        draw_text("This is a rectangle", text_font, (0,0,0), 400,225)

    pygame.display.flip()
        

