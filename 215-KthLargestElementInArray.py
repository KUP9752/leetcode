class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    ## heap
    # heapq.heapify(nums)
    # while len(nums) > k:
    #   heapq.heappop(nums)
    # return nums[0]

    ## sorted
    return sorted(nums, reverse=True)[k - 1]