from collections import defaultdict

class TimeMap:

    def __init__(self):
      self.timeVals = defaultdict(lambda: None)


    def set(self, key: str, value: str, timestamp: int) -> None:
      if not self.timeVals[key]:
        self.timeVals[key] = []

      self.timeVals[key].append((timestamp, value))
      

    def get(self, key: str, timestamp: int) -> str:
      ret = ""
      pairs = self.timeVals[key]

      if not pairs:
        return ret
        
      start = 0
      end = len(pairs) - 1
      while start <= end:
        mid = (start + end) // 2
        setTime = pairs[mid][0]
      
        if setTime <= timestamp:
          ret = pairs[mid][1]
          start = mid + 1
        else: #timestamp < setTime
          end = mid - 1
      return ret
      

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)