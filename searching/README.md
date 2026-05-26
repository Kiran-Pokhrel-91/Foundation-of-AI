# Maze Solver using AI Search Algorithms

A Python maze solver that supports multiple search algorithms:

- DFS (Depth First Search)
- BFS (Breadth First Search)
- Greedy Best-First Search
- A* Search

The project visualizes:
- Walls
- Visited nodes
- Final solution path
- Start and Goal nodes

---

# Features

✅ DFS Search  
✅ BFS Search  
✅ Greedy Best-First Search  
✅ A* Search  
✅ Manhattan Distance Heuristic  
✅ Maze Visualization  
✅ Generic Maze Class  
✅ Path Reconstruction  

---

# Algorithms Included

| Algorithm | Optimal | Uses Heuristic |
|------------|----------|----------------|
| DFS | ❌ | ❌ |
| BFS | ✅ | ❌ |
| Greedy Best First | ❌ | ✅ |
| A* | ✅ | ✅ |

---

# Manhattan Distance Formula

Greedy Best-First Search and A* use Manhattan Distance:

```math
h(n) = |x1 - x2| + |y1 - y2|
```

Where:
- `(x1, y1)` = current node
- `(x2, y2)` = goal node

---

# Project Structure

```bash
project/
│
├── maze1.py
├── maze2.py
├── maze3.py
├── maze4.py
├── searching.txt
└── README.md
```

---

# Maze File Format

Example `maze4.txt`

```text
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
🧱🚩​​🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️🧱
🧱⬜️🧱🧱🧱⬜️🧱🧱🧱⬜️🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱⬜️🧱⬜️🧱
🧱⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱
🧱🧱🧱⬜️🧱🧱🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱
🧱⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱
🧱⬜️🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱⬜️🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱🧱🧱
🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱
🧱🧱🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱⬜️🧱🧱🧱⬜️🧱⬜️🧱⬜️🧱⬜️🧱🧱🧱🧱🧱🧱🧱⬜️🧱
🧱⬜️⬜️⬜️🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️🧱
🧱⬜️🧱⬜️🧱⬜️🧱🧱🧱🧱🧱⬜️🧱🧱🧱🧱🧱⬜️🧱⬜️🧱⬜️🧱🧱🧱🧱🧱🧱🧱⬜️🧱⬜️🧱
🧱⬜️🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱
🧱⬜️🧱⬜️🧱🧱🧱🧱🧱⬜️🧱🧱🧱⬜️🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱
🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱
🧱⬜️🧱🧱🧱🧱🧱⬜️🧱🧱🧱⬜️🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱⬜️🧱
🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱
🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱⬜️🧱
🧱⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️🧱
🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱⬜️🧱⬜️🧱
🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱🏁​​🧱
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
```

## Symbols

| Symbol | Meaning |
|--------|----------|
| A | Start |
| B | Goal |
| Space | Walkable Path |
| Any Other Character | Wall |

---


# Visualization Legend

| Emoji | Meaning |
|--------|----------|
| 🚩 | Start Node |
| 🏁 | Goal Node |
| ⬜️ | Unvisited Node |
| 🟥 | Explored Node |
| 🟩 | Final Path |
| 🧱 | Wall |

---

# Installation

Clone repository:

```bash
git clone <your-repo-url>
cd <repo-name>
```

Make sure Python is installed:

```bash
python --version
```

---

# Usage

```bash
python maze.py maze.txt algorithm
```

---

# Run Examples

## DFS

```bash
python maze.py maze.txt dfs
```

## BFS

```bash
python maze.py maze.txt bfs
```

## Greedy Best First

```bash
python maze.py maze.txt greedy
```

## A*

```bash
python maze.py maze.txt astar
```

---

# Example Output

```text
Solving using DFS...
States Explored: 232
Index...
🚩​​ Starting node 
⬜️ Unvisited node 
🟩 Resulting node 
🟥 Visited node 
🏁​​ Ending node 
Solution:
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
🧱🚩​​🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱🟥🟥🟥🟥🟥🟥🟥🧱🟥🧱
🧱🟩🧱🧱🧱⬜️🧱🧱🧱⬜️🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱⬜️🧱🟥🧱🧱🧱🧱🧱🟥🧱🟥🧱
🧱🟩🟩🟩🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️🧱🟥🟥🟥🟥🟥🧱🟥🟥🟥🧱
🧱🧱🧱🟩🧱🧱🧱🧱🧱⬜️🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱🟥🧱🧱🧱
🧱🟩🟩🟩🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️🟩🟩🟩🟩🟩🟩🟩🟩🟩🧱🟥🟥🟥🟥🟥🟥🟥🧱
🧱🟩🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱🟩🧱🧱🧱⬜️🧱🧱🧱🟩🧱🟥🧱🧱🧱🧱🧱🧱🧱
🧱🟩🟩🟩🟩🟩🧱🟩🟩🟩🟩🟩🟩🟩🧱🟩🟩🟩🧱🟥🟥🟥🧱🟩🧱🟥🟥🟥🟥🟥🟥🟥🧱
🧱🧱🧱🧱🧱🟩🧱🟩🧱🧱🧱🧱🧱🟩🧱🧱🧱🟩🧱🟥🧱🟥🧱🟩🧱🧱🧱🧱🧱🧱🧱🟥🧱
🧱⬜️⬜️⬜️🧱🟩🧱🟩🟩🟩🟩🟩🧱🟩🟩🟩🟩🟩🧱🟥🧱🟥🧱🟩🟩🟩🟩🟩🟩🟩🧱🟥🧱
🧱⬜️🧱⬜️🧱🟩🧱🧱🧱🧱🧱🟩🧱🧱🧱🧱🧱🟥🧱🟥🧱🟥🧱🧱🧱🧱🧱🧱🧱🟩🧱🟥🧱
🧱⬜️🧱⬜️🧱🟩🟩🟩🟩🟩🧱🟩🟩🟩🟥🟥🧱🟥🧱🟥🧱🟥🟥🟥🟥🟥🟥🟥🧱🟩🟥🟥🧱
🧱⬜️🧱⬜️🧱🧱🧱🧱🧱🟩🧱🧱🧱🟩🧱🧱🧱🟥🧱🟥🧱🧱🧱🧱🧱🧱🧱🧱🧱🟩🧱🧱🧱
🧱⬜️🧱⬜️⬜️⬜️⬜️⬜️🧱🟩🟩🟩🧱🟩🟩🟩🧱🟥🧱🟥🟥🟥🟥🟥🟥🟥🟥🟥🧱🟩🟩🟩🧱
🧱⬜️🧱🧱🧱🧱🧱⬜️🧱🧱🧱🟩🧱🧱🧱🟩🧱🟥🧱🧱🧱🧱🧱🧱🧱🧱🧱🟥🧱🧱🧱🟩🧱
🧱⬜️⬜️⬜️⬜️⬜️🧱⬜️⬜️⬜️⬜️🟩🟩🟩🟩🟩🧱🟥🟥🟥🟥🟥🟥🟥🧱🟥🟥🟥🟥🟥🟥🟩🧱
🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱🟥🧱🧱🧱🧱🧱🧱🧱🟩🧱
🧱⬜️⬜️⬜️🧱🟥🟥🟥🟥🟥🟥🟥🧱🟥🟥🟥🟥🟥🟥🟥🟥🟥🧱🟥🟥🟥🟥🟥🟥🟥🧱🟩🧱
🧱⬜️🧱🧱🧱🧱🧱🧱🧱🧱🧱🟥🧱🧱🧱🧱🧱🧱🧱🧱🧱🟥🧱🟥🧱🧱🧱🧱🧱🟥🧱🟩🧱
🧱⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🧱🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🧱🏁​​🧱
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
```

---

# Core Classes

| Class | Purpose |
|--------|----------|
| Node | Represents state in search tree |
| StackFrontier | DFS Frontier |
| QueueFrontier | BFS Frontier |
| GreedyFrontier | Greedy Best-First Frontier |
| AStarFrontier | A* Frontier |
| Maze | Maze Parsing and Solving |

---

# Concepts Covered

This project teaches:

- Graph Search
- Artificial Intelligence Search
- Heuristics
- Pathfinding
- Priority Queues
- Backtracking
- Object-Oriented Programming

---

# Future Improvements

Possible upgrades:

- Dijkstra Algorithm
- Weighted A*
- GUI Visualization
- Pygame Animation
- Random Maze Generator
- Web Version with Django/Flask
- AR Maze Solver

---

# License

MIT License     

Copyright (c) 2026 Kiran Pokhrel

---

# Author

Name: Kiran Pokhrel

# Special Thanks TO:
@ cs50.harvard.edu, For providing excellent material to learn about searching and others algorithm for FREE.