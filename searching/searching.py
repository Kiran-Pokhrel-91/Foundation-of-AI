import sys
import heapq
from collections import deque

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


# DFS Frontier
class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        return self.frontier.pop()



# BFS Frontier
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        return self.frontier.pop(0)


# Greedy Best First Frontier
class GreedyFrontier:
    def __init__(self, goal):
        self.frontier = []
        self.goal = goal
        self.counter = 0

    # Manhattan Distance
    def heuristic(self, state):
        x1, y1 = state
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)

    def add(self, node):
        priority = self.heuristic(node.state)
        heapq.heappush(
            self.frontier,
            (priority, self.counter, node)
        )
        self.counter += 1

    def contains_state(self, state):
        return any(node.state == state for _, _, node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        _, _, node = heapq.heappop(self.frontier)
        return node


# A* Frontier
class AStarFrontier:
    def __init__(self, goal):
        self.frontier = []
        self.goal = goal
        self.counter = 0

    # Manhattan Distance
    def heuristic(self, state):
        x1, y1 = state
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)

    # path cost g(n)
    def path_cost(self, node):
        cost = 0
        while node.parent is not None:
            cost += 1
            node = node.parent
        return cost

    def add(self, node):
        g = self.path_cost(node)
        h = self.heuristic(node.state)
        f = g + h
        heapq.heappush(
            self.frontier,
            (f, self.counter, node)
        )
        self.counter += 1

    def contains_state(self, state):
        return any(node.state == state for _, _, node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        _, _, node = heapq.heappop(self.frontier)
        return node


# MAZE CLASS
class Maze:

    def __init__(self, filename):

        with open(filename) as f:
            contents = f.read()

        # Validate the provided maze
        if contents.count("A") != 1:
            raise Exception("Maze must contain exactly one A")
        if contents.count("B") != 1:
            raise Exception("Maze must contain exactly one B")

        contents = contents.splitlines()

        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
        self.num_explored = 0

    # PRINT MAZE
    def print(self):
        solution = self.solution[1] if self.solution else None
        for i,row in enumerate(self.walls):
            for j,col in enumerate(row):
                if col:
                    print("🧱",end="")
                elif (i,j) == self.start:
                    print("🚩​​",end="")
                elif (i,j) == self.goal:
                    print("🏁​​",end="")
                elif solution is not None and (i,j) in solution :
                    print("🟩",end="")
                elif solution is not None and (i,j) in self.explored :
                    print("🟥",end="")
                else:
                    print("⬜️", end = "")
            print()
        print()

    # GET NEIGHBOURS
    def neighbours(self, state):

        row, col = state

        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []

        for action, (r, c) in candidates:

            if 0 <= r < self.height and 0 <= c < self.width:

                if not self.walls[r][c]:

                    result.append((action, (r, c)))

        return result

   # solve function to solve maize
    def solve(self, algorithm="dfs"):

        self.num_explored = 0
        start = Node(state=self.start,parent=None,action=None)

        # Chooseing the required Algorithm
        if algorithm == "dfs":
            frontier = StackFrontier()
        elif algorithm == "bfs":
            frontier = QueueFrontier()
        elif algorithm == "greedy":
            frontier = GreedyFrontier(self.goal)
        elif algorithm == "astar":
            frontier = AStarFrontier(self.goal)
        else:
            raise Exception("Invalid Algorithm")
        
        frontier.add(start)
        self.explored = set()

        while True:
            if frontier.empty():
                raise Exception("No Solution")

            node = frontier.remove()
            self.num_explored += 1

            # Goal Test and reverse tracking
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explored.add(node.state)

            # Expand
            for action, state in self.neighbours(node.state):
                if (not frontier.contains_state(state) and state not in self.explored):
                    child = Node(state=state,parent=node,action=action)
                    frontier.add(child)


if len(sys.argv) != 3:
    sys.exit("Usage: python maze.py maze.txt algorithm" )
filename = sys.argv[1]
algorithm = sys.argv[2]

m = Maze(filename)

print("Maze:")
m.print()

print(f"Solving using {algorithm.upper()}...")
m.solve(algorithm)

print("States Explored:", m.num_explored)

print("Index...")
print(f"🚩​​ Starting node ")
print(f"⬜️ Unvisited node ")
print(f"🟩 Resulting node ")
print(f"🟥 Visited node ")
print(f"🏁​​ Ending node ")

print("Solution:")
m.print()