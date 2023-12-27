class Solution:
  def islandPerimeter(self, grid: list[list[int]]) -> int:
    WATER = 0
    LAND = 1
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    dirs = [1, -1]
    
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == LAND:
          perimeter += 4
          
        ## check up down
          for di in dirs:
            x = i + di
            if x in range(rows) and grid[x][j] == LAND:
              perimeter -= 1
          ## check right left
          for dj in dirs:
            y = j + dj
            if y in range(cols) and grid[i][y] == LAND:
              perimeter -= 1
    return perimeter
  
  def islandPerim2(self, grid: list[list[int]]) -> int:
    WATER = 0
    LAND = 1
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == LAND:
          perimeter += 4
          
          ## check only behind (up and left)
          up = i - 1
          if up >= 0 and grid[up][j] == LAND:
            perimeter -= 2
          left = j - 1
          if left >= 0 and grid[i][left] == LAND:
            perimeter -= 2
    return perimeter