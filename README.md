# Syntecxhub Week 1: Maze Solver using A* Search

## Project Overview
As part of my AI Internship at **Syntecxhub**, this project demonstrates the implementation of the **A* (A-Star) Search Algorithm** to find the shortest path within a maze. The program models a grid where certain cells are walkable paths and others are obstacles (walls).

## Features
- **Pathfinding:** Calculates the most efficient route from a Start point to a Goal point.
- **Heuristics:** Utilizes **Manhattan Distance** to estimate the cost to reach the goal.
- **Efficiency:** Uses a **Priority Queue (Heap)** for optimal node expansion.
- **Visualization:** Generates a clear, wide-format plot showing the maze, walls, and the calculated path using `matplotlib`.

## Technical Details
The algorithm uses the core A* formula:
$$f(n) = g(n) + h(n)$$
- **g(n):** The cost of the path from the start node to node $n$.
- **h(n):** The heuristic estimate of the cost from node $n$ to the goal.

## How to Run
1. Clone the repository:
   `git clone https://github.com/YOUR_USERNAME/Syntecxhub_Maze_Solver.git`
2. Install dependencies:
   `pip install matplotlib numpy`
3. Run the script:
   `python maze_solver.py`

## 🎮 How to Play
- **Left Click:** Place the **Start** (Green), **Goal** (Blue), and **Walls** (Black).
- **Right Click:** Erase nodes or walls.
- **Spacebar:** Watch the AI find the shortest path in real-time.
- **'C' Key:** Clear the grid and start over.

## Setup
1. Clone this repo: `git clone https://github.com/YOUR_USERNAME/Syntecxhub_Maze_Solver.git`
2. Install dependencies: `pip install pygame`
3. Run the game: `python maze_solver.py`

---
**Intern:** Ammara Tahir  
[cite_start]**Internship Provider:** [Syntecxhub](https://www.syntecxhub.com) [cite: 59]
---
