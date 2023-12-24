class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:

    def bruteForce() -> List[List[int]]:
      res = set()
      for i, ni in enumerate(nums):
        for j, nj in enumerate(nums):
          for k, nk in enumerate(nums):
            if i != j and i != k and j != k and ni + nj + nk == 0:
              res.add(tuple(sorted((ni, nj, nk))))
      return res

    def optimised() -> List[List[int]]:
      res = []
      snums = sorted(nums)
      n = len(snums)
      seen = [False for _ in range(n)]
      for i, ni in enumerate(snums):
        if i > 0 and ni == snums[i - 1]:
          continue
        left = i + 1
        right = n - 1
        while left < right:
          nj = snums[left]
          nk = snums[right]
          tot = ni + nj + nk
          if tot < 0:
            left += 1
          elif tot > 0:
            right -= 1
          else: ## found 0 need to find more answers
            res.append([ni, nj, nk])
            left += 1
            while snums[left] == snums[left - 1] and left < right:
              left += 1
      return res
    return optimised()    


