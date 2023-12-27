class Solution:
  def numDecodings(self, s: str) -> int:
    n = len(s)
    dp = [0 for _ in range(n + 1)]
    dp[n] = 1
    
    for i in range(len(s) - 1, -1, -1): #last index -> 0 (incl)
      if s[i] != "0":
        dp[i] = dp[i + 1]
      
      if i + 1 < n and \
         (s[i] == "1" or \
         s[i] == "2" and s[i + 1] in "0123456"):
          dp[i] += dp[i + 2]
    
    return dp[0]

