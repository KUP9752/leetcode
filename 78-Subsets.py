class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    subsets = []
    n = len(nums)
    
    def go(startIdx: int, temps: List[int], res: List[List[int]]) -> None:
      res.append(temps)
      for i in range(startIdx, n):
        go(i + 1, temps + [nums[i]], res)


    go(0, [], subsets)
    return subsets


