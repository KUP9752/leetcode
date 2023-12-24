class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    def countAdder(string: str) -> dict[chr, int]:
      hashmap = dict()
      for c in string:
        if c in hashmap:
          hashmap[c] += 1
        else: 
          hashmap.update({c : 1})
      return hashmap
    
    return countAdder(s) == countAdder(t)

