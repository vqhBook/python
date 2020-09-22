import time
import pygame

def draw():
    screen.fill(PINK)
    text = font.render(f"{num_moves}", True, DARK_GRAY, PINK)
    screen.blit(text, (screen.get_rect().centerx - text.get_rect().width//2, h))
    for rod, rod_x in zip([A, B, C], [w, int(2.5*w), 4*w]):
        pygame.draw.rect(screen, MAROON, (rod_x - 5, 4*h, 10, (n + 1)*h))
        y = screen.get_rect().height
        for disk in rod:
            disk_w = int((0.3 + 0.7*disk/n) * w)
            disk_color = (0, 0, int(disk/n*255))
            pygame.draw.rect(screen, disk_color, (rod_x - disk_w//2, y - h, disk_w, h - 1))
            y -= h
    pygame.display.update()

def move(num_disk, rod1, rod2, rod3):
    global num_moves
    
    if num_disk == 0:
        return
    move(num_disk - 1, rod1, rod3, rod2)
    rod2.append(rod1.pop())
    num_moves += 1
    draw(); time.sleep(1)
    move(num_disk - 1, rod3, rod2, rod1)

n = 5
w, h = 200, 25
MAROON = (128, 0, 0)
PINK = (255, 192, 203)
DARK_GRAY = (169,169,169)

pygame.init()
screen = pygame.display.set_mode((5*w, (n + 5)*h))
pygame.display.set_caption("Ha Noi Tower")
font = pygame.font.SysFont(None, 2*h)

A, B, C = list(range(n, 0, -1)), [], []
num_moves = 0
draw(); time.sleep(1)
move(n, A, B, C)

input("Press Enter to quit. ")
pygame.quit()
