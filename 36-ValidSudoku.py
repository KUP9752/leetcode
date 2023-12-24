class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    validNums = "123456789"
    boxSide = 3
    gameSide = 9

    ## Function calls slow it down, but can't be asked to fix it

    def isValid(nums: List[int]) -> bool:
      for c in validNums:
        if nums.count(c) > 1:
          return False
      return True

    def isValidBox(startX: int, startY: int) -> bool:
      box = [board[x][y] for x in range(startX, startX + boxSide) for y in range(startY, startY + boxSide)]
      return isValid(box)
      
    def isValidRow(index: int) -> bool:
      row = board[index]
      return isValid(row)
      
    def isValidCol(index: int) -> bool:
      col = [row[index] for row in board]
      return isValid(col)

    
    # Validate rows and cols
    for idx in range(gameSide):
      if not isValidRow(idx): 
        return False
      if not isValidCol(idx):
        return False
    #Validate boxes
    for x in range(0, gameSide, boxSide):
      for y in range(0, gameSide, boxSide):
        if not isValidBox(x, y):
          return False
    return True



