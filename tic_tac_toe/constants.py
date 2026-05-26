import pygame

# SCREEN SIZE
WIDTH = 600
HEIGHT = 600

# GRID
ROWS = 3
COLS = 3

# CELL SIZE
SQSIZE = WIDTH // COLS

# OFFSET FOR SHAPES
OFFSET = int(SQSIZE // 3.8)

# COLORS (
BG_COLOR = pygame.Color("#79e8e7")
LINE_COLOR = pygame.Color("#000000")
X_COLOR = pygame.Color("#4A4848")
O_COLOR = pygame.Color("#ffffff")
WIN_LINE_COLOR = pygame.Color("#107c10")  
BUTTON_COLOR = pygame.Color("#252525")
TEXT_COLOR = pygame.Color("#ffffff")

# LINE THICKNESS
LINE_WIDTH = 5  
X_LINE_WIDTH = 15
CIRCLE_WIDTH = 15