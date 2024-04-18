class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    ## Constraints: O(n) and 5no division allowed
    res = [1 for _ in range(len(nums))]
    
    for i in range(1, len(nums)):
      res[i] = nums[i-1] * res[i - 1]
      
    acc = 1
    for i in range(len(nums) - 1, -1, -1):
      res[i] *= acc
      acc *= nums[i]
    
    return res
    
  def slow2_productExceptSelf(self, nums: list[int]) -> list[int]:
    ## Constraints: O(n) and 5no division allowed
    
    befores = [1 for _ in range(len(nums))]
    afters  = [1 for _ in range(len(nums))]
    
    n = len(nums)
    for i in range(n - 1): ## loops: [0, n - 2]
      ## befores: [1 -> n - 1]
      ## afters: [n - 2 -> 0]
      print(f"{i = }")
      
      befores[i + 1] = nums[i] * befores[i]
      afters[n - 2 - i] = nums[n - 1 - i] * afters[n - 1 - i]
    
    return [befores[i] * afters[i] for i in range(len(nums))]
    
  def slow_productExeptSelf(self, nums:list[int]) -> list[int]:
    befores = [1 for i in range(len(nums))]
    afters  = [1 for i in range(len(nums))]
    
    for i in range(1, len(nums)):
      befores[i] = nums[i - 1] * befores[i - 1]
    
    for i in range(len(nums) - 2, -1, -1):
      afters[i] = nums[i + 1] * afters[i + 1]
      
    return [befores[i] * afters[i] for i in range(len(nums))]
    
    
sol = Solution()
tests = [
  [1,2,3,4],
  [-1,1,0,-3,3],
  []
]
answers = [
  [24, 12, 8, 6],
  [0,0,9,0,0],
  []
]
for (test, ans) in zip(tests, answers):
  res = sol.productExceptSelf(test)
  print("=====")
  print(f"{res = }")
  print(f"{test = } => {"PASSED" if ans == res else "FAILED"}")
  