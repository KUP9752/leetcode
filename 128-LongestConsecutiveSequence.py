class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    visited = defaultdict(bool)
    ranges = defaultdict(list) # stores int -> (l, r) range pair
    longest = 0
    for i in nums:
      if visited[i]: continue

      visited[i] = True
      l, r = i, i
      if ranges[i - 1]:
        l = ranges[i - 1][0]
      if ranges[i + 1]:
        r = ranges[i + 1][1]
      ranges[l] = [l, r]
      ranges[r] = [l, r]
      longest = max(longest, r - l + 1)
    return longest


