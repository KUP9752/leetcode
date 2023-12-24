class Solution:
  def search(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    res = -1
 
    while start <= end:
      if start == end and target == nums[start]:
        res = start
        break
      mid = (start + end) // 2
      ## we are in the left
      if nums[mid] >= nums[start]:
        if target > nums[mid]:
          start = mid + 1
        else: #target < middle
          if target < nums[start]:
            start = mid + 1
          else: #target >= start
            end = mid
      ## we are on the right
      else: 
        if target <= nums[mid]:
          end = mid
        else: #target > middle
          if target < nums[start]:
            start = mid +1
          else: #target >= num[start]
            end = mid





    return res
