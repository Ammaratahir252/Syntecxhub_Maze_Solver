import heapq
import pygame

# --- Neon Theme Configuration ---
WIDTH = 900 
HEIGHT = 650
GRID_AREA = 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Syntecxhub AI Lab: Minimalist Neon Solver")

# Color Palette
BG_DARK = (18, 18, 18)      
NEON_GREEN = (57, 255, 20)  # Start
NEON_BLUE = (0, 255, 255)   # End
NEON_RED = (255, 49, 49)    # Shortest Path
NEON_WALL = (255, 215, 0)   # Neon Gold Walls

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row, self.col = row, col
        self.x, self.y = row * width, col * width
        self.color = BG_DARK
        self.neighbors = []
        self.width, self.total_rows = width, total_rows

    def get_pos(self): return self.row, self.col

    def draw(self, win):
        margin = 1
        pygame.draw.rect(win, self.color, (self.x + margin, self.y + margin, self.width - margin*2, self.width - margin*2), border_radius=3)

    def make_start(self): self.color = NEON_GREEN
    def make_end(self): self.color = NEON_BLUE
    def make_wall(self): self.color = NEON_WALL
    def make_path(self): self.color = NEON_RED
    def reset(self): self.color = BG_DARK
    def is_wall(self): return self.color == NEON_WALL

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            self.neighbors.append(grid[self.row][self.col - 1])

def h(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star_algorithm(draw, grid, start, end):
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}; g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}; f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
        
        current = heapq.heappop(open_set)[2]
        open_set_hash.remove(current)

        if current == end:
            while current in came_from:
                current = came_from[current]
                if current != start: # Keep start green
                    current.make_path()
            start.make_start(); end.make_end()
            draw() # Draw final path only
            return True

        for neighbor in current.neighbors:
            temp_g = g_score[current] + 1
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
    return False

def draw_sidebar(win):
    pygame.draw.rect(win, (25, 25, 25), (650, 0, 250, HEIGHT))
    font = pygame.font.SysFont("Segoe UI", 24, bold=True)
    small_font = pygame.font.SysFont("Segoe UI", 18)
    
    win.blit(font.render("AI PATHFINDER", True, NEON_BLUE), (670, 40))
    
    controls = [
        ("Left Click", "Start/End/Walls"),
        ("Right Click", "Reset Square"),
        ("SPACE", "Find Shortest Path"),
        ("C Key", "Clear Screen")
    ]
    
    for i, (key, desc) in enumerate(controls):
        win.blit(small_font.render(key, True, NEON_RED), (670, 100 + i*60))
        win.blit(small_font.render(desc, True, (200, 200, 200)), (670, 125 + i*60))

def main():
    pygame.font.init()
    ROWS, SIZE = 25, 650
    grid = [[Node(i, j, SIZE//ROWS, ROWS) for j in range(ROWS)] for i in range(ROWS)]
    start, end, run = None, None, True

    while run:
        WIN.fill(BG_DARK)
        for row in grid:
            for node in row: node.draw(WIN)
        
        draw_sidebar(WIN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            
            if pygame.mouse.get_pressed()[0]: # Left Click
                pos = pygame.mouse.get_pos()
                if pos[0] < SIZE:
                    r, c = pos[0]//(SIZE//ROWS), pos[1]//(SIZE//ROWS)
                    if 0 <= r < ROWS and 0 <= c < ROWS:
                        node = grid[r][c]
                        if not start and node != end: start = node; start.make_start()
                        elif not end and node != start: end = node; end.make_end()
                        elif node != end and node != start: node.make_wall()

            elif pygame.mouse.get_pressed()[2]: # Right Click
                pos = pygame.mouse.get_pos()
                if pos[0] < SIZE:
                    r, c = pos[0]//(SIZE//ROWS), pos[1]//(SIZE//ROWS)
                    if 0 <= r < ROWS and 0 <= c < ROWS:
                        node = grid[r][c]
                        node.reset()
                        if node == start: start = None
                        if node == end: end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row: node.update_neighbors(grid)
                    a_star_algorithm(lambda: [n.draw(WIN) for r in grid for n in r] or pygame.display.update(), grid, start, end)
                if event.key == pygame.K_c:
                    start, end = None, None
                    grid = [[Node(i, j, SIZE//ROWS, ROWS) for j in range(ROWS)] for i in range(ROWS)]

    pygame.quit()

if __name__ == "__main__": main()