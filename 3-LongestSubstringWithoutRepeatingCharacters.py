class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    left = right = 0
    maxLen = 0
  
    # print(f"len {len(s)}")
    # print(f"first {s[0]}")
    # print(f"right: {right}")
    curr = set()
    while right < len(s):
      c = s[right]
      
      if c not in curr:
        curr.add(c)
        right += 1
      else:
        maxLen = max(maxLen, len(curr))
        curr.clear()
        left += 1
        right = left
      # print(f"curr: {curr}")
    return max(maxLen, len(curr))

      # curr = 1
      # if s[right] not in s[left:right]:
      #   curr += 1
      # else:
      #   left = right
      #   maxLen = max(curr, maxLen)
      # right += 1
    