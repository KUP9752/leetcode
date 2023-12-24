class Solution:
  def findMin(self, nums: List[int]) -> int:
    def twoPointers() -> int:
      n = len(nums)
      left = 0
      right = n - 1
      while nums[left] > nums[right]:
        right -= 1
      return nums[(right + 1) % n]

    def binSearch() -> int:
      n = len(nums)
      start = 0
      end = n - 1
      while start < end:
        mid = (start + end) // 2

        if nums[end] < nums[mid]:
          start = mid + 1
        elif nums[end] > nums[mid]:
          end = mid
        ## else case is omitted, items are unique
      ## loop returns when start == end finding us the starting (minimum number)
      return nums[start]

    # return twoPointers()
    return binSearch()
