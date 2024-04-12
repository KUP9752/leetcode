class Solution:
  def isHappy(self, n: int) -> bool:
    seen = set()
    seen.add(n)
    
    while True:
      digSum = self.adder(n)
      if digSum == 1: return True
      if digSum in seen: return False
      
      seen.add(digSum)
      n = digSum
  def adder(self, n: int) -> int:
    base = 10
    total = 0
    
    while (n != 0):
      digit = n % base 
      n = n // base
      total += digit ** 2
    print(f"{total = }")
    
    return total

sol = Solution()
print(f"{sol.isHappy(19) = }")
print(f"{sol.isHappy(2) = }")

      
      