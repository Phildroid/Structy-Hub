def minimum_island(grid):
  visited = set()
  min_size = float('inf')

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      current_island = explore_len(grid, r, c, visited)
      if current_island > 0:
        min_size = min(min_size, current_island)
  return min_size

def explore_len(grid, r, c, visited):
  island_len = 0
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return False
  if grid[r][c] == 'W':
    return False
  pos = (r, c)
  if pos in visited:
    return False
  visited.add(pos)
  island_len = 1

  island_len += explore_len(grid, r + 1, c, visited)
  island_len += explore_len(grid, r - 1, c, visited)
  island_len += explore_len(grid, r, c + 1, visited)
  island_len += explore_len(grid, r, c - 1, visited)
  
  return island_len
