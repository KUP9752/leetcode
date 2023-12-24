class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    ##find row
    start = 0
    end = len(matrix)
    row = None
    # return False
    while start < end: 
      mid = (end + start) // 2

      ##lower row
      if target < matrix[mid][0]:
        end = mid
      ## higher row
      elif target > matrix[mid][-1]:
        start = mid + 1
      ## row found
      else:
        row = mid
        break

    if row is None:
      return False
      
    start = 0 
    end = len(matrix[row])
    while start < end:
      mid = (start + end) // 2
      
      ##found
      if target == matrix[row][mid]:
        return True

      if target < matrix[row][mid]:
        end = mid
        # return True
      else:
        start = mid + 1
    
    return False