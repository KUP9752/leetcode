class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    ## if there is only one bit set then power of 2
    return n > 0 and n & (n - 1) == 0
    
      