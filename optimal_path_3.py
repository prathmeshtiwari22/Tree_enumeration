import random
import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define grid size
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20

def create_grid(width, height, density):
  """Creates a 2D grid with obstacles based on density."""
  grid = []
  for row in range(height):
    grid_row = []
    for col in range(width):
      if random.random() < density:
        grid_row.append(1)  # Obstacle
      else:
        grid_row.append(0)  # Empty space
    grid.append(grid_row)
  return grid

def heuristic(a, b):
  """Manhattan distance heuristic."""
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
  """A* search algorithm to find optimal path."""
  came_from = {}
  g_score = {cell: float('inf') for row in grid for cell in row}
  g_score[start] = 0
  f_score = {cell: float('inf') for row in grid for cell in row}
  f_score[start] = heuristic(start, goal)
  open_set = {start}

  while open_set:
    current = min(open_set, key=lambda x: f_score[x])
    if current == goal:
      return reconstruct_path(came_from, current)

    open_set.remove(current)
    for (x, y) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
      neighbor = (current[0] + x, current[1] + y)
      if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != 1:
        tentative_g_score = g_score[current] + 1
        if tentative_g_score < g_score.get(neighbor, float('inf')):
          came_from[neighbor] = current
          g_score[neighbor] = tentative_g_score
          f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
          if neighbor not in open_set:
            open_set.add(neighbor)
  return None  # No path found

  """A* search algorithm to find optimal path."""
  came_from = {}
  g_score = {cell: float('inf') for row in grid for cell in row}
  g_score[start] = 0
  f_score = {cell: float('inf') for row in grid for cell in row}
  f_score[start] = heuristic(start, goal)
  open_set = {start}

  while open_set:
    current = min(open_set, key=lambda x: f_score[x])
    if current == goal:
      return reconstruct_path(came_from, current)

    open_set.remove(current)
    for (x, y) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
      neighbor = (current[0] + x, current[1] + y)
      if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != 1:
        tentative_g_score = g_score[current] + 1
        if tentative_g_score < g_score[neighbor]:
          came_from[neighbor] = current
          g_score[neighbor] = tentative_g_score
          f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
          if neighbor not in open_set:
            open_set.add(neighbor)
  return None  # No path found

def reconstruct_path(came_from, current):
  """Reconstructs the optimal path from came_from dictionary."""
  path = [current]
  while current in came_from:
    current = came_from[current]
    path.append(current)
  return path[::-1]  # Reverse path

def draw_grid(grid, surface):
  """Draws the grid on the pygame window."""
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      color = WHITE if grid[row][col] == 0 else BLACK
      pygame.draw.rect(surface, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_path(path, surface):
  """Draws the optimal path on the pygame window."""
  for i in range(len(path) - 1):
    x1, y1 = path[i]
    x2, y2 = path[i + 1]
    pygame.draw.line(surface, GREEN, (x1 * CELL_SIZE + CELL_SIZE // 2, y1 * CELL_SIZE + CELL_SIZE // 2),
                     (x2 * CELL_SIZE + CELL_SIZE // 2, y2 * CELL_SIZE + CELL_SIZE // 2), width=2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("A* Pathfinding")

    # Map with random obstacles
    grid = create_grid(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE, 0.2)  # Adjust density as needed

    # Define start and goal nodes
    start = (0, 4)  # Edit starting coordinates
    goal = (WIDTH // CELL_SIZE - 1, HEIGHT // CELL_SIZE - 1)  # Edit goal coordinates

    # Find path using A*
    path = a_star(grid, start, goal)

    # Draw grid and path (if exists)
    draw_grid(grid, screen)
    if path:
        draw_path(path, screen)
    else:
        print("No path found!")

    # Event handling loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
