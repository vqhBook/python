import pygame
import random, time

TETROMINOS = {
    "I": { "box": [[0, -1, -1, 0, 0],
                   [-1, -1, -1, 0, 0],
                   [1, 1, 1, 1, -1],
                   [0, 0, -1, -1, -1],
                   [0, 0, -1, -1, 0]],
           "size": (5, 5),              # width, height
           "center": (1.5, 2.5)         # xc, yc
           },
    "T": { "box": [[0, 0, -1, 0, 0],
                   [0, -1, 1, -1, 0],
                   [-1, 1, 1, 1, -1],
                   [0, 0, -1, -1, 0],
                   [0, 0, -1, 0, 0]],
           "size": (5, 5),
           "center": (2.0, 2.0)
           },
    "J": { "box": [[0, -1, -1, -1, 0],
                   [0, 1, -1, -1, 0],
                   [-1, 1, 1, 1, -1],
                   [0, 0, -1, -1, 0],
                   [0, 0, -1, 0, 0]],
           "size": (5, 5),
           "center": (2.0, 2.0)
           },
    "L": { "box": [[0, 0, -1, 0, 0],
                   [0, -1, -1, 1, -1],
                   [-1, 1, 1, 1, -1],
                   [0, 0, -1, -1, -1],
                   [0, 0, -1, 0, 0]],
           "size": (5, 5),
           "center": (2.0, 2.0)
           },
    "O": { "box": [[0, -1, -1, 0, 0],
                   [-1, 1, 1, -1, 0],
                   [-1, 1, 1, -1, 0],
                   [0, -1, -1, 0, 0],
                   [0, 0, 0, 0, 0]],
           "size": (5, 5),
           "center": (1.5, 1.5)
           },
    "S": { "box": [[0, 0, -1, 0, 0],
                   [0, -1, 1, 1, -1],
                   [-1, 1, 1, -1, -1],
                   [0, 0, -1, -1, -1],
                   [0, 0, 0, 0, 0]],
           "size": (5, 5),
           "center": (2.0, 2.0)
           },
    "Z": { "box": [[0, -1, -1, -1, 0],
                   [0, 1, 1, -1, 0],
                   [0, -1, 1, 1, -1],
                   [0, 0, -1, -1, 0],
                   [0, 0, -1, 0, 0]],
           "size": (5, 5),
           "center": (2.0, 2.0)
           }
    }

class Settings:
    def __init__(self):
        self.back_color = (255, 192, 203)       # Pink
        self.inf_back_color =(169, 169, 169)    # Dark Gray 
        self.text_color = (0, 0, 0)             # Black
        self.nexttet_color = (255, 69, 0)       # Orangered
        self.matrix_color = (0, 0, 128)         # Navy
        self.tet_color = (0, 0, 255)            # Blue
        self.gameover_color = (255, 0, 0)       # Red

        self.move_sound = pygame.mixer.Sound("sound_move.wav")
        self.rotate_sound = pygame.mixer.Sound("sound_rotate.wav")
        self.landing_sound = pygame.mixer.Sound("sound_landing.wav")
        self.match_sound = pygame.mixer.Sound("sound_match.wav")
        self.play_sound = pygame.mixer.Sound("sound_play.wav")
        self.pause_sound = pygame.mixer.Sound("sound_pause.wav")
        self.gameover_sound = pygame.mixer.Sound("sound_gameover.wav")
        
        self.cell_width = 28 # pixels
        self.width, self.height, self.inf_width = 10, 20, 7 # cells
        self.font_scale = 1
        self.level = 1
        self.score = 0
        self.nextlvscore = 50
        self.speed = 1.0    # 1s/move
        self.music_on = True

        self.KEY_DIR = {pygame.K_RIGHT: (0, 1), pygame.K_LEFT: (0, -1),
                        pygame.K_DOWN: (1, 0)}
    def incr_score(self, totalrow):
        self.score += totalrow * 10 + (totalrow - 1) * 5
        if self.score >=  self.nextlvscore:
            self.level += 1
            self.nextlvscore += 50
            self.speed *= 0.6

class Board:
    def _map(self, pos):
        xc, yc = TETROMINOS[self.tet]["center"]
        if self.tetdir == 90:
            return (int(pos[1] - xc + yc), int(-pos[0] + yc + xc))
        elif self.tetdir == 180:
            return (int(-pos[0] + 2*yc), int(-pos[1] + 2*xc))
        elif self.tetdir == 270:
            return (int(-pos[1] + xc + yc), int(pos[0] - yc + xc))
        else:
            return pos
        
    def _nexttet(self):
        self.tet = self.next_tet
        self.tetrow = -2
        self.tetcol = self.sett.width//2 - TETROMINOS[self.tet]["size"][0]//2
        self.tetdir = 0
        self.next_tet = random.choice(list(TETROMINOS))
        return self._canmove((0, 0))
        
        
    def _canmove(self, pos): # r, c
        for r in range(TETROMINOS[self.tet]["size"][1]):
            for c in range(TETROMINOS[self.tet]["size"][0]):
                if TETROMINOS[self.tet]["box"][r][c] == 1:
                    nr, nc = self._map((r, c))
                    nr += self.tetrow + pos[0]
                    nc += self.tetcol + pos[1]
                    if nr >= self.sett.height or nc not in range(self.sett.width) \
                       or (nr >= 0 and self.matrix[nr][nc]) == 1:
                        return False
        return True

    def _canrotate(self):
        for r in range(TETROMINOS[self.tet]["size"][1]):
            for c in range(TETROMINOS[self.tet]["size"][0]):
                if TETROMINOS[self.tet]["box"][r][c] == -1:
                    nr, nc = self._map((r, c))
                    nr += self.tetrow
                    nc += self.tetcol
                    if nr >= self.sett.height or nc not in range(self.sett.width) \
                       or (nr >= 0 and self.matrix[nr][nc] == 1):
                        return False
        return True

    def _rotate(self):
        self.tetdir = (self.tetdir + 90) % 360

    def _fixtet(self):
        self.sett.landing_sound.play()
        
        for r in range(TETROMINOS[self.tet]["size"][1]):
            for c in range(TETROMINOS[self.tet]["size"][0]):
                if TETROMINOS[self.tet]["box"][r][c] == 1:
                    nr, nc = self._map((r, c))
                    nr += self.tetrow
                    nc += self.tetcol
                    if nr in range(self.sett.height) and nc in range(self.sett.width):
                        self.matrix[nr][nc] = 1

        self.clearing = True
        nfullrow = 0
        row = self.sett.height - 1
        while row >= 0:
            if all([self.matrix[row][col] == 1 for col in range(self.sett.width)]):
                nfullrow += 1
                for col in range(self.sett.width):
                    self.matrix[row][col] = 0
                self.draw_board()
                pygame.display.update()
                self.sett.match_sound.play()
                time.sleep(0.30)
                for ra in range(row - 1, -1, -1):
                    for col in range(self.sett.width):
                        self.matrix[ra + 1][col] = self.matrix[ra][col]
                self.draw_board()
                pygame.display.update()
                time.sleep(0.30)
            else:
                row -= 1
        self.clearing = False

        if nfullrow > 0:
            self.sett.incr_score(nfullrow)
                    
    def rand_item_cell(self):
        while True:
            x, y = random.randint(0, self.sett.width - 1), random.randint(0, self.sett.height - 1)
            if (x, y) not in self.snake_cells:
                return (x, y)

    def draw_cell(self, cell, color): # (r, c)
        pygame.draw.rect(self.screen, color,
            (cell[1] * self.sett.cell_width + 1, cell[0] * self.sett.cell_width + 1, self.sett.cell_width - 2, self.sett.cell_width - 2))

    def draw_board(self):
        self.screen.fill(self.sett.inf_back_color)
        pygame.draw.rect(self.screen, self.sett.back_color,
                         (0, 0, self.sett.width * self.sett.cell_width, self.sett.height * self.sett.cell_width))    
        
        text = self.font.render(f"Level: {self.sett.level}", True, self.sett.text_color, self.sett.inf_back_color)
        self.screen.blit(text, ((self.sett.width + 1) * self.sett.cell_width, 6 * self.sett.font_scale * self.sett.cell_width))
        text = self.font.render(f"Score: {self.sett.score}", True, self.sett.text_color, self.sett.inf_back_color)
        self.screen.blit(text, ((self.sett.width + 1) * self.sett.cell_width, 7 * self.sett.font_scale * self.sett.cell_width))
        text = self.font.render(f"Next: {self.sett.nextlvscore}", True, self.sett.text_color, self.sett.inf_back_color)
        self.screen.blit(text, ((self.sett.width + 1) * self.sett.cell_width, 8 * self.sett.font_scale * self.sett.cell_width))
        text = self.font.render(f"Music (M): {'On' if self.sett.music_on else 'Off'}", True, self.sett.text_color, self.sett.inf_back_color)
        self.screen.blit(text, ((self.sett.width + 1) * self.sett.cell_width, 9 * self.sett.font_scale * self.sett.cell_width))

        # draw next tet
        for r in range(TETROMINOS[self.next_tet]["size"][1]):
            for c in range(TETROMINOS[self.next_tet]["size"][0]):
                if TETROMINOS[self.next_tet]["box"][r][c] == 1:
                    self.draw_cell((r + 1, c + self.sett.width + 1), self.sett.nexttet_color)
                    
        # draw matrix
        for r in range(self.sett.height):
            for c in range(self.sett.width):
                if self.matrix[r][c] == 1:
                    self.draw_cell((r, c), self.sett.matrix_color)

        # draw cur tet
        if not self.clearing:
            for r in range(TETROMINOS[self.tet]["size"][1]):
                for c in range(TETROMINOS[self.tet]["size"][0]):
                    if TETROMINOS[self.tet]["box"][r][c] == 1:
                        nr, nc = self._map((r, c))
                        nr += self.tetrow
                        nc += self.tetcol
                        if nr in range(self.sett.height) and nc in range(self.sett.width):
                            self.draw_cell((nr, nc), self.sett.tet_color)

        text = None
        if self.gameover:
            text = self.font.render(f"Game over! Score: {self.sett.score}", True, self.sett.gameover_color, self.sett.back_color)
        elif self.pausing:
            text = self.font.render("Press Space to Play/Pause", True, self.sett.text_color, self.sett.back_color)

        if text is not None:
            text_rect = text.get_rect()
            text_rect.centerx = self.sett.width * self.sett.cell_width // 2
            text_rect.centery = self.sett.height * self.sett.cell_width // 2
            self.screen.blit(text, text_rect)

    def _start(self):
        self.sett = Settings()
        self.matrix = [[0 for w in range(self.sett.width)] for h in range(self.sett.height)]
        self.next_tet = random.choice(list(TETROMINOS))
        self._nexttet()
        self.pausing = True
        self.clearing = False
        self.gameover = False
            
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1, 0)
        self._start()
        self.screen = pygame.display.set_mode(((self.sett.width + self.sett.inf_width) * self.sett.cell_width, self.sett.height * self.sett.cell_width))
        pygame.display.set_caption("Tetris Game")
        self.font = pygame.font.SysFont(None, self.sett.font_scale * self.sett.cell_width)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.gameover:
                            self._start()
                        else:
                            self.pausing = not self.pausing
                            if self.pausing:
                                self.sett.pause_sound.play()
                            else:
                                self.sett.play_sound.play()
                        if not self.pausing:
                            start_time = time.time()
                    if event.key == pygame.K_m:
                        self.sett.music_on = not self.sett.music_on
                        if self.sett.music_on:
                            pygame.mixer.music.play(-1, 0)
                        else:
                            pygame.mixer.music.stop() 
                    if not self.pausing:
                        if (event.key in self.sett.KEY_DIR) and self._canmove(self.sett.KEY_DIR[event.key]):
                            # move
                            self.sett.move_sound.play()
                            self.tetcol += self.sett.KEY_DIR[event.key][1]
                            self.tetrow += self.sett.KEY_DIR[event.key][0]
                        if event.key == pygame.K_UP and self._canrotate():
                            # rotate
                            self.sett.rotate_sound.play()
                            self._rotate()

            if not self.pausing:
                tm = time.time()
                if tm - start_time >= self.sett.speed:
                    if self._canmove((1, 0)):
                        self.tetrow += 1
                    elif self._fixtet():
                        # tang level
                        self.incr_score()
                    elif not self._nexttet():
                        # gameover
                        self.sett.gameover_sound.play()
                        self.pausing = True
                        self.gameover = True
                    start_time = time.time()
                
            self.draw_board()
            pygame.display.update()

    def quit(self):
        pygame.quit()
        print("Bye!")

board = Board()
board.run()
board.quit()
