class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      def dist(x: int, y: int) -> int:
        return math.sqrt(x**2 + y**2)
      ## Non-heap solution
      # return sorted(points, key=lambda p: dist(p[0],p[1]))[:k]  
      def tripleDist(x:int, y:int) -> (int, int, int):
        return math.sqrt(x**2 + y**2), x, y

      ps = [tripleDist(x, y) for x, y in points]
      heapq.heapify(ps)
      res = []
      for _ in range(k):
        triple = heapq.heappop(ps)
        x, y = triple[1], triple[2]
        res.append([x, y])
      return res
      
