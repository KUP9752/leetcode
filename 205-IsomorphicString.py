from collections import defaultdict

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    
    mappings = defaultdict(lambda : None)
    
    for i in range(len(s)):
      if mappings[s[i]] and mappings[s[i]] != t[i]: 
        ## mapping exist but it is not the same
        return False
      mappings[s[i]] = t[i]
    
    vals = mappings.values()
    ## no two chars can map to the same char
    return len(vals) == len(set(vals))
      
sol = Solution()
print(f"{sol.isIsomorphic("egg", "add") = }")
print(f"{sol.isIsomorphic("foo", "bar") = }")
print(f"{sol.isIsomorphic("badc", "baba") = }")

