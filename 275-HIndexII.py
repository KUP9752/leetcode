class Solution:
  ## sprted list of citations, must be done in O(logn)
  def hIndex(self, citations: list[int]) -> int:
    n = len(citations)
    ## try in range[0..n] but in a binary searh way
    
    right = n - 1
    left = 0
    
    while left <= right:
      mid = right + left // 2
      ## shows there is atleast papers with h (= n - mid) 
      ## citations before this one
      if citations[mid] == n - mid:
        return n - mid
      elif citations[mid] < n - mid:
        left = mid + 1
      ## there arent enough papers before hand with citations
      else:
        right = mid - 1
    return n - left 
      



    
sol = Solution()
tests = [
  [0,1,3,5,6], 
  [1,1,3],
  [1, 2, 100],
  [0, 0, 4, 4]
]
results = [
  3,
  1,
  2,
  2
]

for (test, res) in zip(tests, results):
  print(f"For {test = }")
  print(f"\t{sol.hIndex(test) = }")
  print(f"\t?: {sol.hIndex(test) == res = }")
  

      