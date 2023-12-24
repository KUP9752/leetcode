class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    start1 = -1
    start2 = 0
    for i in range(n):
      match nums[i]:
        case 0:
          if start1 != -1 and start1 < n:
            nums[start1], nums[i] = nums[i], nums[start1]
            start1 +=1
          if start2 < n:
            nums[start2], nums[i] = nums[i], nums[start2]
            start2 += 1
        case 1: 
          if start1 == -1: 
            start1 = start2
          if start2 < n:
            nums[start2], nums[i] = nums[i], nums[start2]
            start2 += 1

      




