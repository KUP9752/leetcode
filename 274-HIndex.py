class Solution: 
  def hIndex(self, citations: list[int]) -> int:
    ## possible values of h index is [0, n]
    n = len(citations) # number of papers
    
    sortedCs = sorted(citations) # sort ascending
    
    for h in range(n, 0, -1):
      i = n - h #normmalises index bacward
      if h <= sortedCs[i]:
        return h
    return 0
  
  def fasterHIndex(self, citations: list[int]) -> int:
    n = len(citations)
    freqs = [0 for _ in range(n + 1)] # to be able to store n
    
    for citation in citations:
      c = citation if citation <= n else n
      freqs[c] += 1
    
    count = 0
    for i in range(n, -1, -1):
      count += freqs[i]
      if count >= i:
        return i
    return 0
        
sol = Solution()
tests = [
  [3,0,6,1,5], 
  [1,3,1],
  [100],
  [5,5,4],
  [4,4,0,0]
]

for test in tests:
  print(f"For {test = }")
  print(f"\t{sol.hIndex(test) = }")
  print(f"\t{sol.fasterHIndex(test) = }")
  print(f"\tSame? {sol.hIndex(test) == sol.fasterHIndex(test) = }")
  

      