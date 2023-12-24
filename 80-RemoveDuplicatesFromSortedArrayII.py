class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    fast = 1
    slow = 0
    count = 1
  
    while fast < n:
      if nums[slow] == nums[fast]:
        count += 1
        ## same num in sequence, see how many we found so far
        if count == 2:
          ## if we have seen 2 move slow to point to end of sequence
          ## also swap here
          slow += 1
          nums[slow], nums[fast] = nums[fast], nums[slow]
      else:
        ## not matching, must do swapping
        slow += 1 # next location from slow is where new num should be swapped into
        nums[slow], nums[fast] = nums[fast], nums[slow]
        count = 1 #we now see one of the new number
      fast += 1
    
    return slow + 1