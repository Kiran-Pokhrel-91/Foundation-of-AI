import pygame
from constants import *

class Renderer:
    """Handles all drawing and visual rendering operations."""
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont("arial", 30, bold=True)

    def center(self, r, c):
        return c * SQSIZE + SQSIZE // 2, r * SQSIZE + SQSIZE // 2

    def grid(self):
        for i in range(1, ROWS):
            pygame.draw.line(self.surface, LINE_COLOR, (i * SQSIZE, 0), (i * SQSIZE, HEIGHT), LINE_WIDTH)
            pygame.draw.line(self.surface, LINE_COLOR, (0, i * SQSIZE), (WIDTH, i * SQSIZE), LINE_WIDTH)

    def x(self, r, c):
        x, y = self.center(r, c)
        o = OFFSET
        pygame.draw.line(self.surface, X_COLOR, (x - o, y - o), (x + o, y + o), X_LINE_WIDTH)
        pygame.draw.line(self.surface, X_COLOR, (x + o, y - o), (x - o, y + o), X_LINE_WIDTH)

    def o(self, r, c):
        x, y = self.center(r, c)
        pygame.draw.circle(self.surface, O_COLOR, (x, y), OFFSET, CIRCLE_WIDTH)

    def win_line(self, line):
        if not line: return
        t, i = line

        if t == "row":
            y = i * SQSIZE + SQSIZE // 2
            pygame.draw.line(self.surface, WIN_LINE_COLOR, (0, y), (WIDTH, y), 10)
        elif t == "col":
            x = i * SQSIZE + SQSIZE // 2
            pygame.draw.line(self.surface, WIN_LINE_COLOR, (x, 0), (x, HEIGHT), 10)
        elif t == "diag":
            if i == 1:
                pygame.draw.line(self.surface, WIN_LINE_COLOR, (0, 0), (WIDTH, HEIGHT), 10)
            else:
                pygame.draw.line(self.surface, WIN_LINE_COLOR, (WIDTH, 0), (0, HEIGHT), 10)

    def overlay(self):
        s = pygame.Surface((WIDTH, HEIGHT))
        s.set_alpha(160)
        s.fill((0, 0, 0))
        self.surface.blit(s, (0, 0))

    def text(self, msg):
        img = self.font.render(msg, True, TEXT_COLOR)
        rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        self.surface.blit(img, rect)

    def button(self, text, rect_obj):
        pygame.draw.rect(self.surface, BUTTON_COLOR, rect_obj)
        img = self.font.render(text, True, TEXT_COLOR)
        self.surface.blit(img, img.get_rect(center=rect_obj.center))