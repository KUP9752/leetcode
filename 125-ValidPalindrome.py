class Solution:
  alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
  def isPalindrome(self, s: str) -> bool:
    
    # onlyAlpha = [c for c in s.lower() if c in alpha]
    # # def recChecker(toCheck: str, start: int, end: int) -> bool:
    # #   if start >= end: return True

    # #   return toCheck[start] == toCheck[end] and recChecker(toCheck, start + 1, end - 1)
    # n = len(onlyAlpha)

    # for i in range(n):
    #   if onlyAlpha[i] != onlyAlpha[n - i - 1]: return False

    # return True
    # # return onlyAlpha == onlyAlpha[::-1]

    x = 0  #pointer to front
    y = len(s) - 1 #pointer to back
    return self.check(s, x, y)

  def check(self, s: str, i: int, j: int) -> bool:
      ## find char from front
      c1 = s[i].lower()
      while c1 not in self.alpha and i < len(s) - 1:
        # print(f"c1: {c1}")
        i += 1
        c1 = s[i].lower()
      print(f"c1,i: {c1},{i}")

      ## find char from back
      c2 = s[j].lower()
      while c2 not in self.alpha and j > 0:
        j -= 1
        c2 = s[j].lower()
      print(f"c2,j: {c2},{j}")
      if i >= j:
        return True
      if c1 == c2:
        return self.check(s, i + 1, j - 1)
      return False



