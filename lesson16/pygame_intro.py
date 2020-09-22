import time
import pygame

w = 20
pygame.init()
screen = pygame.display.set_mode((60*w, 6*w))
pygame.display.set_caption("Welcome to Pygame")

WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
ORANGE_RED = (255, 69, 0)
MAROON = (128, 0, 0)
PINK = (255, 192, 203)

(car := pygame.Surface((9*w, 5*w))).fill(WHITE)
pygame.draw.polygon(car, DARK_GREEN, [(3*w, 0), (6*w, 0), (7*w, int(1.5*w)),
    (9*w, 2*w), (9*w, 4*w), (0, 4*w), (0, int(2.5*w)), (2*w, int(1.5*w))])
pygame.draw.rect(car, ORANGE_RED, (3*w, w, int(1.2*w), 2*w))
pygame.draw.rect(car, ORANGE_RED, (int(4.8*w), w, int(1.2*w), 2*w))
pygame.draw.circle(car, MAROON, (2*w, 4*w), w)
pygame.draw.circle(car, PINK, (2*w, 4*w), w//2)
pygame.draw.circle(car, MAROON, (7*w, 4*w), w)
pygame.draw.circle(car, PINK, (7*w, 4*w), w//2)

x = -9*w
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    screen.blit(car, (x, w))
    pygame.display.update()
    time.sleep(0.005)
    x += 1
    if x > 60*w:
        x = -9*w

pygame.quit()
