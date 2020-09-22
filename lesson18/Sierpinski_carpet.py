import pygame

def Sierpinski(x0, y0, w, level):
    if level == stop_level:
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                pygame.draw.rect(screen, WHITE, (x0 + w//3, y0 + w//3, w//3, w//3))
            else:
                Sierpinski(x0 + i*w//3, y0 + j*w//3, w//3, level + 1)
    
width = 600
stop_level = 5
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

pygame.init()
screen = pygame.display.set_mode((width, width))
pygame.display.set_caption("Sierpinski carpet")

screen.fill(PINK)
Sierpinski(0, 0, width, 0)
pygame.display.update()

input("Press Enter to quit. ")
pygame.quit()
