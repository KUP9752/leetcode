class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    paths = [[0 for _ in range(n)] for _ in range(m)]
    paths[0][0] = 1
    for i in range(0,m):
      for j in range(0,n):
        if i == 0 or j == 0:
          paths[i][j] = 1
        else:
          paths[i][j] = (paths[i][j -1] if j else 0) + (paths[i - 1][j] if i else 0)
    return paths[-1][-1]





    # paths = [[-1 for _ in range(n)] for _ in range(m)]

    # def memo(i: int, j: int) -> int:
    #   if (i == m - 1 or j == n - 1):
    #     paths[i][j] = 1
    #     return 1
    #   elif paths[i][j] != -1:
    #     return paths[i][j]
    #   else:
    #     temp = memo(i + 1, j) + memo(i, j + 1)
    #     paths[i][j] = temp
    #     return temp

    # return memo(0, 0)
    
  
