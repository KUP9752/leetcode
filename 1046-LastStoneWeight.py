class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
      y = heapq.heappop(stones)
      x = heapq.heappop(stones)

      if x != y:
        y = y - x ## no need for abs, we need to insert it back
        heapq.heappush(stones, y)
    if stones:
      return abs(stones[0])
    return 0




      

