class Solution:
  def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
    currMax = 0
    curr = divisors[0]
    for i, div in enumerate(divisors):
      count = 0
      for j, num in enumerate(nums):
        count = count + 1 if (num % div == 0) else count
      divisors[i] = count
      # selection logic
      if (currMax == count):
        curr = div if (div < curr) else curr
      elif (currMax < count):
        currMax = count
        curr = div

    return curr

