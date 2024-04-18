class Solution:
  def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    z = 0 # pointer keeping track of the zero
    for i in range(len(nums)):
      if nums[i] != 0:
        nums[z], nums[i] = nums[i], nums[z]
        z += 1
  
  def moveZeroesO2(self, nums: list[int]) -> None:
    def move(i: int, nums: list[int]) -> None:
      for j in range(i + 1, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    
    for i in range(len(nums)):
      if nums[i] == 0:
        move(i, nums)
    
  def checkZeroes(self, nums: list[int]) -> list[int]:
    self.moveZeroes(nums)
    return nums
      
sol = Solution()
tests = [
  [0,1,0,3,12],
  [0],
  []
]
answers = [
  [1,3,12,0,0],
  [0],
  []
]

for (test, ans) in zip(tests, answers):
  res = sol.checkZeroes(test)
  print(f"{test = } => {"PASSED" if test == res else "FAILED"}")
  