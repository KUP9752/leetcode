class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #pointers to first and last numbers
    ## !! ORDERED
    i = 0
    j = len(numbers) - 1

    #search until middle
    while i <= j:
      ## remove large if greater, else move up
      total = numbers[i] + numbers[j] 
      if total == target:
        return [i + 1, j + 1]
      elif total > target:
        j -= 1
      else:
        i += 1
    return [-1, -1] ##not found, not possible for this question!

  


      
