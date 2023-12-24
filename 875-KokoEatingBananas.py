import math

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def isDoable(piles: List[int], k: int, h: int) -> bool:
      totTime = 0
      for pile in piles:
        totTime += math.ceil(pile / k)

      return totTime <= h

    def bruteForce() -> int:
      maxK = max(piles)
      minK = 1
      for k in range(minK, maxK + 1):
        if isDoable(piles, k, h):
          return k

    def binarySearch() -> int:
      ### ks are in increasing order
      # ks = [k + 1 for k in range(max(piles))]
      start = 1
      end = max(piles)
      while start < end:
        mid = (start + end) // 2
        isK = isDoable(piles, mid, h)
        ## not doable search lower end
        if isK:
          end = mid
        ## doable but is it min?
        else:
          start = mid + 1
      ## loop terminates when start == end, so min is found at start
      return start
      


      
    return binarySearch()

        