import pygame
import random
import heapq

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define grid parameters
ROWS = 20
COLS = 20
WIDTH = 600
HEIGHT = 600
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

# A* algorithm
def heuristic(start, goal):
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])

def astar(grid, start, goal):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start))
    came_from = {}

    g_score = {cell: float('inf') for row in grid for cell in row}
    g_score[start] = 0
    f_score = {cell: float('inf') for row in grid for cell in row}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        closed_set.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_set or grid[neighbor[0]][neighbor[1]] == 1:
                continue

            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start))
    came_from = {}

    g_score = {cell: float('inf') for row in grid for cell in row}
    g_score[start] = 0
    f_score = {cell: float('inf') for row in grid for cell in row}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        closed_set.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_set or grid[neighbor[0]][neighbor[1]] == 1:
                continue

            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def get_neighbors(cell):
    neighbors = []
    row, col = cell
    if row > 0:
        neighbors.append((row - 1, col))
    if row < ROWS - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < COLS - 1:
        neighbors.append((row, col + 1))
    return neighbors

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Algorithm")

# Create a random map with obstacles
density = 0.3  # Adjust this value to control obstacle density
grid = [[0 if random.random() < density else 1 for _ in range(COLS)] for _ in range(ROWS)]
start = (0, 0)
goal = (ROWS - 1, COLS - 1)

# Find the optimal path using A*
path = astar(grid, start, goal)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if grid[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
            pygame.draw.rect(screen, BLACK, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 1)

    # Draw the start and goal nodes
    pygame.draw.circle(screen, RED, (start[1] * CELL_WIDTH + CELL_WIDTH // 2, start[0] * CELL_HEIGHT + CELL_HEIGHT // 2), 10)
    pygame.draw.circle(screen, GREEN, (goal[1] * CELL_WIDTH + CELL_WIDTH // 2, goal[0] * CELL_HEIGHT + CELL_HEIGHT // 2), 10)

    # Draw the optimal path
    if path:
        for cell in path:
            pygame.draw.circle(screen, GREEN, (cell[1] * CELL_WIDTH + CELL_WIDTH // 2, cell[0] * CELL_HEIGHT + CELL_HEIGHT // 2), 5)

    pygame.display.flip()

pygame.quit()
