class Solution:
  def search(self, nums: List[int], target: int) -> int:
    # start = 0
    # end = len(nums)
    # n = end - start
    # while n != 0:
    #   mid = (n // 2) + start
      
    #   if target == nums[mid]:
    #     return mid
    #   if target < nums[mid]:
    #     end = mid
    #   else:
    #     start = mid + 1

    #   n = end - start
    # return -1

    start = 0
    end = len(nums)
    while start < end: 
      mid = (start + end) // 2

      if target == nums[mid]:
        return mid
      elif target < nums[mid]:
        end = mid
      else: #target > nums[mid]
        start = mid + 1
    return -1 ##error not found
    

