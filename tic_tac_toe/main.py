import sys
import pygame
import numpy as np

from constants import *
from ai_engine import GameTreeAI
from ui_renderer import Renderer

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.grid = np.zeros((ROWS, COLS))
        self.moves = 0

    def place(self, r, c, player):
        self.grid[r][c] = player
        self.moves += 1

    def empty(self, r, c):
        return self.grid[r][c] == 0

    def full(self):
        return self.moves == 9

    def winner(self):
        g = self.grid
        for r in range(ROWS):
            if g[r][0] == g[r][1] == g[r][2] != 0: return g[r][0]
        for c in range(COLS):
            if g[0][c] == g[1][c] == g[2][c] != 0: return g[0][c]
        if g[0][0] == g[1][1] == g[2][2] != 0: return g[0][0]
        if g[0][2] == g[1][1] == g[2][0] != 0: return g[0][2]
        return None

    def win_line(self):
        g = self.grid
        for r in range(ROWS):
            if g[r][0] == g[r][1] == g[r][2] != 0: return ("row", r)
        for c in range(COLS):
            if g[0][c] == g[1][c] == g[2][c] != 0: return ("col", c)
        if g[0][0] == g[1][1] == g[2][2] != 0: return ("diag", 1)
        if g[0][2] == g[1][1] == g[2][0] != 0: return ("diag", 2)
        return None


class Game:
    def __init__(self, surface):
        self.board = Board()
        self.renderer = Renderer(surface)
        self.ai = GameTreeAI()

        self.player = 1
        self.running = True
        self.winner = None
        self.win_line = None
        self.mode = "MENU"
        
        self.pvp_btn = pygame.Rect(200, 250, 200, 60)
        self.ai_btn = pygame.Rect(200, 330, 200, 60)
        self.restart_btn = pygame.Rect(200, 330, 200, 60)

    def reset(self):
        self.board.reset()
        self.player = 1
        self.running = True
        self.winner = None
        self.win_line = None
        self.mode = "MENU"

    def draw_pieces(self):
        for r in range(ROWS):
            for c in range(COLS):
                if self.board.grid[r][c] == 1:
                    self.renderer.x(r, c)
                elif self.board.grid[r][c] == 2:
                    self.renderer.o(r, c)

    def play(self, r, c):
        if not self.running or not self.board.empty(r, c):
            return

        self.board.place(r, c, self.player)
        self.check_end()

        if not self.running:
            return

        if self.mode == "PVP":
            self.player = 2 if self.player == 1 else 1
        elif self.mode == "AI":
            move = self.ai.find_best_move(self.board.grid)
            if move:
                self.board.place(move[0], move[1], 2)
                self.check_end()

    def check_end(self):
        self.winner = self.board.winner()
        self.win_line = self.board.win_line()
        if self.winner or self.board.full():
            self.running = False

    def menu(self):
        self.renderer.overlay()
        self.renderer.button("P2P MODE", self.pvp_btn)
        self.renderer.button("AI MODE", self.ai_btn)

    def end_screen(self):
        self.renderer.overlay()
        if self.winner == 1:
            msg = "PLAYER 1 WINS"
        elif self.winner == 2:
            msg = "AI WINS" if self.mode == "AI" else "PLAYER 2 WINS"
        else:
            msg = "DRAW"
        self.renderer.text(msg)
        self.renderer.button("RESTART", self.restart_btn)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tree Tic Tac Toe")
    
    game = Game(screen)
    clock = pygame.time.Clock()

    while True:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.mode == "MENU":
                    if game.pvp_btn.collidepoint(event.pos):
                        game.mode = "PVP"
                    elif game.ai_btn.collidepoint(event.pos):
                        game.mode = "AI"

                elif game.mode in ["PVP", "AI"] and game.running:
                    r = event.pos[1] // SQSIZE
                    c = event.pos[0] // SQSIZE
                    if 0 <= r < ROWS and 0 <= c < COLS:
                        game.play(r, c)

                elif not game.running:
                    if game.restart_btn.collidepoint(event.pos):
                        game.reset()

        game.renderer.grid()
        game.draw_pieces()
        game.renderer.win_line(game.win_line)

        if game.mode == "MENU":
            game.menu()
        if not game.running:
            game.end_screen()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()