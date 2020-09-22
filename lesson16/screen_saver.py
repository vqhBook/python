import time, random
import pygame

def draw_random_rectangle():
    sw, sh = screen.get_size()
    x, y = random.randrange(sw), random.randrange(sh)
    width, height = random.randrange(sw - x), random.randrange(sh - y) 
    color = (random.randrange(256), random.randrange(256), random.randrange(0, 256))
    pygame.draw.rect(screen, color, (x, y, width, height), 0)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

screen.fill((255, 192, 203)) # PINK
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            running = False

    draw_random_rectangle()
    pygame.display.update()
    time.sleep(0.25)

pygame.quit()
