import random, time
import pygame

class Settings:
    def __init__(self):
        self.back_color = (255, 192, 203)   # Pink
        self.text_color = (169,169,169)     # Dark Gray
        self.head_color = (0,0,128)         # Navy
        self.body_color = (0,0,255)         # Blue
        self.item_color = (255,69,0)        # Orangered
        self.gameover_color = (255, 0, 0)   # Red
        
        self.cell_width = 15                # pixels
        self.width, self.height = 50, 25    # cells
        self.font_scale = 2
        
        self.level = 1
        self.score = 0
        self.speed = 0.3                    # s/move

        self.DELTA = {"Right": (1, 0), "Left": (-1, 0),
                      "Up": (0, -1), "Down": (0, 1)}
        self.KEY_DIR = {pygame.K_RIGHT: ("Left", "Right"),
                        pygame.K_LEFT: ("Right", "Left"),
                        pygame.K_UP: ("Down", "Up"),
                        pygame.K_DOWN: ("Up", "Down")}

    def incr_score(self):
        self.score += 1
        if self.score % 5 == 0:
            self.level += 1
            self.speed *= 0.8


class Board:
    def __init__(self):
        self._setup()
        pygame.init()
        self._screen = pygame.display.set_mode(
            (self.sett.width * self.sett.cell_width,
             self.sett.height * self.sett.cell_width))
        pygame.display.set_caption("Snake Game")
        self._font = pygame.font.SysFont(None,
            self.sett.font_scale * self.sett.cell_width)

    def _setup(self):
        self.sett = Settings()
        self._snake_cells = [(self.sett.width//2 + d,
            self.sett.height//2) for d in range(-1, 2)]
        self._item_cell = self._rand_item_cell()
        self._direction = "Right"
        self._pausing = True
        self._gameover = False
        
    def _rand_item_cell(self):
        while True:
            x, y = (random.randint(0, self.sett.width - 1),
                    random.randint(0, self.sett.height - 1))
            if (x, y) not in self._snake_cells:
                return (x, y)

    def _draw_board(self):
        self._screen.fill(self.sett.back_color)
        if self._gameover:
            text = self._font.render(
                f"Game over! Score: {self.sett.score}. Press Space to Play", True,
                self.sett.gameover_color, self.sett.back_color)
        elif self._pausing:
            text = self._font.render(
                "Press Space to Play/Pause", True,
                self.sett.text_color, self.sett.back_color)
        else:
            text = self._font.render(
                f"Level: {self.sett.level} - Score: {self.sett.score}", True,
                self.sett.text_color, self.sett.back_color)
        
        text_rect = text.get_rect()
        text_rect.centerx = self._screen.get_rect().centerx
        text_rect.centery = self.sett.font_scale * self.sett.cell_width
        self._screen.blit(text, text_rect)

        if self._gameover:
            self._draw_cell(self._snake_cells[-1],
                            self.sett.gameover_color)
        else:
            self._draw_cell(self._snake_cells[-1],
                            self.sett.head_color)
            self._draw_cell(self._item_cell,
                            self.sett.item_color)
        for i in range(len(self._snake_cells) - 1):
            self._draw_cell(self._snake_cells[i],
                            self.sett.body_color)

    def _draw_cell(self, cell, color):
        pygame.draw.rect(self._screen, color,
            (cell[0] * self.sett.cell_width,
             cell[1] * self.sett.cell_width,
             self.sett.cell_width, self.sett.cell_width))

    def _move_snake(self, direction):
        next_x = (self._snake_cells[-1][0]
                  + self.sett.DELTA[direction][0])
        next_y = (self._snake_cells[-1][1]
                  + self.sett.DELTA[direction][1])
        if (next_x not in range(self.sett.width)
            or next_y not in range(self.sett.height)
            or (next_x, next_y) in self._snake_cells):
            return False

        self._snake_cells.append((next_x, next_y))
        if self._item_cell == (next_x, next_y):
            self._item_cell = self._rand_item_cell()
            self.sett.incr_score()
        else:
            self._snake_cells.pop(0)
        return True

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self._gameover:
                            self._setup()
                        else:
                            self._pausing = not self._pausing
                            if not self._pausing:
                                start_time = time.time()
                    if (not self._pausing
                        and event.key in self.sett.KEY_DIR):
                        if self._direction != self.sett.KEY_DIR[event.key][0]:
                            self._direction = self.sett.KEY_DIR[event.key][1]

            if not self._pausing:
                tm = time.time()
                if tm - start_time >= self.sett.speed:
                    if self._move_snake(self._direction):
                        start_time = time.time()
                    else: # Gameover
                        self._pausing = True
                        self._gameover = True
                
            self._draw_board()
            pygame.display.update()

    def quit(self):
        pygame.quit()
        print("Bye!")

board = Board()
board.run()
board.quit()
