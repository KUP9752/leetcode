class Solution: 
  def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
    LAND = 1
    WATER = 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    islandSizes: list[int] = [0] ## 0 if no islands
    seen: set[(int, int)] = set()
    
    def traverse(i: int, j: int) -> None:
      """ Base Cases:
        1) We are not in the grid (implciitly water)
        2) this square is a water square
        3) We have already visited
        Only traverse if cases aren't met!
      """
      if not (i not in range(rows) or # 1)
              j not in range(cols) or # 1)
              grid[i][j] == WATER or # 2)
              (i, j) in seen): # 3)
        seen.add((i, j))
        
        ## increase size for this component
        islandSizes[-1] += 1
        
        ## Then traverse all adjacent just incase there is more land connected
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          traverse(i + di, j + dj)
          
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == LAND and (i, j) not in seen:
          islandSizes.append(0) ## starts a new island counter
          traverse(i, j)
    
    return max(islandSizes)
          