class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    def go(nums, temps, res) -> None:
      if not nums:
        res.append(temps)
      for i in range(len(nums)):
        go(nums[:i] + nums[i+1:], temps + [nums[i]], res)
        
    ps = []
    go(nums, [], ps)
    return ps
