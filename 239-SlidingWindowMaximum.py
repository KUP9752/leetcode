from collections import deque

class Solution:
  def slidingWindowMaximum(self, nums: list[int], k: int) -> list[int]:
    maxs = []
    queue = deque() ## keeps the indices of the maximums
    fast = slow = 0
    
    ## Once the window is filled move window by 1
    while fast < len(nums):
      ## cannot be maximum of current window if newest is larger than prev
      while queue and nums[fast] > nums[queue[-1]]: 
        queue.pop()
        
      queue.append(fast) ## possible new max value
      
      
      ## element no longer relevant in the current window
      if slow > queue[0]:
        queue.popleft()
      
      ## move window if the window is filled (reached size k)
      if fast + 1 >= k:
        maxs.append(nums[queue[0]])
        slow += 1
      fast += 1  
      
    return maxs
      
        
  def TLE_slidingWindowMaximum(self, nums: list[int], k: int) -> list[int]:
    maxs = []
    rep = 0
    while rep + k <= len(nums):
      maxs.append(max(nums[rep : rep + k]))
      rep += 1
    
    return maxs
  
sol = Solution()
tests = [
  ([1,3,-1,-3,5,3,6,7], 3),
  ([1], 1),
  ([11,11],2),
  ([1, -1], 1)
]
answers = [
  [3, 3, 5, 5, 6, 7],
  [1],
  [11],
  [1,-1]
]
for (test, ans) in zip(tests, answers):
  p1, p2 = test
  print("=====")
  res = sol.slidingWindowMaximum(p1, p2)
  print(f"{res = }")
  print(f"{test = } => {"PASSED" if res == ans else "FAILED"}")
  