import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Draw with Pygame")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen.fill(WHITE)
drawing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                pos = event.pos
            else:
                screen.fill(WHITE)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False

    if drawing:
        newpos = pygame.mouse.get_pos()
        pygame.draw.line(screen, RED, pos, newpos, 1)
        pos = newpos

    pygame.display.update()    

pygame.quit()
