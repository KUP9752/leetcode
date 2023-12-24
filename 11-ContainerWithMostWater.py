class Solution:
  def maxArea(self, height: List[int]) -> int:
    def bruteForce() -> int:## Brute Force
      currMax = 0
      n = len(height)
      for i in range(n):
        for j in range(i + 1, n):
          currMax = max(currMax, min(height[i], height[j]) * abs(i - j))
      return currMax

    def optimised() -> int:
      currMax = 0
      n = len(height)
      left = 0
      right = n - 1

      while left <= right:
        currMax = max(currMax, min(height[left], height[right]) * abs(left - right))
        if height[left] < height[right]:
          left += 1
        else:
          right -= 1
      return currMax

    return optimised()
