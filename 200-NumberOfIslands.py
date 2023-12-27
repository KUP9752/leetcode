
class Solution:
    
  def numIslands(self, grid: list[list[str]]) -> int:
    LAND = "1"
    WATER = "0"
    
    rows = len(grid)
    cols = len(grid[0]) ## same for all rows
    
    count = 0
    seen = set()
    
    ## given i, j find all the connected land masses
    def traverse(i: int, j: int):
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
        ## Then traverse all adjacent just incase there is more land connected
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          traverse(i + di, j + dj)
      
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == LAND and (i, j) not in seen:
          count += 1
          traverse(i, j)
    return count 
    