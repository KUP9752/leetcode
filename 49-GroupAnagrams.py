class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      def isAnagram(s: str, other: str) -> bool:
        for c in "abcdefghijklmnopqrstuvwxyz":
          if s.count(c) != other.count(c):
            return False
        return True
      
      groups = defaultdict(list)

      for s in strs:
        sortedKey = ''.join(sorted(s))
        groups[sortedKey].append(s)
      return groups.values()

      def TimeLimitExceeder2() -> List[List[str]]:
        used: Set[int] = set() # checked indices
        groups: Dict[str, List[str]] = {}
        addedFlag = False
        for i, s in enumerate(strs):
          if i in used:
            continue
          for key in groups.keys():
            if isAnagram(key, s):
              groups[key].append(s)
              addedFlag = True
          if not addedFlag:
            groups.update({s : [s]})
          addedFlag = False
          used.add(i)
        return groups.values()

      return TimeLimitExceeder2()

      # def TimeLimitExceeder() -> List[List[str]]:
      #   groups: List[List[str]] = []
      #   while len(strs) != 0:
      #     # print(f"strs:{strs}")
          
      #     head = strs.pop(0)
      #     # anagrams.append(head)
      #     # print(f"strs:{strs}")
      #     # print(f"head: {head}")
      #     rest = [s for s in strs if isAnagram(head, s)]
      #     # for s in strs:
      #     #   print(f"s, i: {s},{i}")
      #     #   if isAnagram(head, s):
      #     #     anagrams.append(s)
      #     #     # strs.remove(s)
      #     # print(f"strs:{strs}")
      #     # print(f"rest: {rest}")
      #     strs = [s for s in strs if s not in rest]
      #     # print(f"rest: {rest}")
      #     anagrams = rest
      #     anagrams.append(head)
      #     # print(f"anagrams: {anagrams}")
      #     groups.append(anagrams)
      #     # print()

      #   return groups


