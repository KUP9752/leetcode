class Solution:
  def longestPalindrome(self, s: str) -> str:
    maxLen = 0
    subPal = ""

    for i in range(len(s)):
      
      for left, right in [(i,i), (i, i + 1)]:
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
          newLen = right - left + 1
          if newLen > maxLen:
            maxLen = newLen
            subPal = s[left:right + 1]
          left -= 1
          right += 1
        
    return subPal