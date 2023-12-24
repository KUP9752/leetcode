class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    fast = 0
    slow = 0
    n = len(nums)

    while fast < n:
      ## advance fast until new number found
      ## fast found the next value in order, swap slow + 1 with fast
      if nums[slow] != nums[fast]:
        ## slow now points to last of the sorted place (k - 1)
        slow += 1
        nums[slow], nums[fast] = nums[fast], nums[slow]
      fast += 1
    return slow + 1

