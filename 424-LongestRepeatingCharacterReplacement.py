class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

      maxLen = 0
      left = 0
      counts = defaultdict(lambda: 0)
      mostFreq = 0

      for right in range(len(s)):
        c = s[right]
        counts[c] += 1
        mostFreq = max(mostFreq, counts[c])
        while (right - left + 1) - mostFreq > k:
          counts[s[left]] -= 1
          left += 1
        
        maxLen = max(maxLen, right - left + 1)
      return maxLen
  