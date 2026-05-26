import numpy as np
from constants import ROWS, COLS

class GameNode:
    """Represents a single state of the board in our search tree."""
    def __init__(self, board_grid):
        self.grid = np.copy(board_grid)
        self.children = {}  # Maps move coordinate (r, c) -> GameNode
        self.score = 0

    def get_empty_cells(self):
        empty_spaces = []
        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c] == 0:
                    empty_spaces.append((r, c))
        return empty_spaces

    def check_winner(self):
        g = self.grid
        for r in range(ROWS):
            if g[r][0] == g[r][1] == g[r][2] != 0: return g[r][0]
        for c in range(COLS):
            if g[0][c] == g[1][c] == g[2][c] != 0: return g[0][c]
        if g[0][0] == g[1][1] == g[2][2] != 0: return g[0][0]
        if g[0][2] == g[1][1] == g[2][0] != 0: return g[0][2]
        return None

    def is_terminal(self):
        return self.check_winner() is not None or len(self.get_empty_cells()) == 0


class GameTreeAI:
    """Calculates next moves by searching through GameNodes."""
    def build_and_score_tree(self, node, is_maximizing):
        if node.is_terminal():
            winner = node.check_winner()
            if winner == 2:    return 1   # AI won
            elif winner == 1:  return -1  # Human won
            else:              return 0   # Draw

        if is_maximizing:
            best_score = -100
            for move in node.get_empty_cells():
                next_grid = np.copy(node.grid)
                next_grid[move[0]][move[1]] = 2
                
                child_node = GameNode(next_grid)
                node.children[move] = child_node
                
                score = self.build_and_score_tree(child_node, False)
                if score > best_score:
                    best_score = score
            node.score = best_score
            return best_score
        else:
            best_score = 100
            for move in node.get_empty_cells():
                next_grid = np.copy(node.grid)
                next_grid[move[0]][move[1]] = 1
                
                child_node = GameNode(next_grid)
                node.children[move] = child_node
                
                score = self.build_and_score_tree(child_node, True)
                if score < best_score:
                    best_score = score
            node.score = best_score
            return best_score

    def find_best_move(self, current_grid):
        root = GameNode(current_grid)
        
        if len(root.get_empty_cells()) == 8:
            return (1, 1) if root.grid[1][1] == 0 else (0, 0)

        self.build_and_score_tree(root, True)

        best_move = None
        best_value = -100
        for move, child in root.children.items():
            if child.score > best_value:
                best_value = child.score
                best_move = move
                
        return best_move