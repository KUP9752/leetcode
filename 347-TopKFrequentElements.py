class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    occurs = {}
    for num in nums:
      if num in occurs:
        occurs[num] += 1
      else:
        occurs.update({num : 1})
    
    ordered = sorted(occurs.items(), key = lambda pair: pair[1], reverse=True)
    # print(ordered)
    # print( list(map(lambda pair: pair[0], ordered[:k])))
    return list(map(lambda pair: pair[0], ordered[:k]))
        