class Solution:
  def rob(self, nums: List[int]) -> int:
    def robNoCircle(nums: List[int]) -> int:
      if not nums:
        return 0
      
      n = len(nums)
      if n == 1:
        return nums[0]

      dp = [0  for _ in range(n)]
      dp[0] = nums[0]
      dp[1] = nums[1]
      for i in range(2, n):
        dp[i] = nums[i] + max(dp[i - 2], dp[i-3])
      return max(dp[n-2], dp[n-1])
    if not nums:
      return 0
    if len(nums) == 1:
      return nums[0]
    return max(robNoCircle(nums[1:]), robNoCircle(nums[:-1]))