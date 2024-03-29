class Solution:
  def isUgly(self, n:int) -> bool:
    if n == 0: 
      return False
    if n in [1, 2, 3, 5]:
      return True
      
    isDiv2 = n % 2 == 0
    isDiv3 = n % 3 == 0
    isDiv5 = n % 5 == 0
    
    return (
      isDiv2 and self.isUgly(n / 2) or
      isDiv3 and self.isUgly(n / 3) or
      isDiv5 and self.isUgly(n / 5) 
    )
    
sol = Solution()
def checkUgly(n: int) -> None:
  ugly = "ugly" if sol.isUgly(n) else "not ugly"
  print(f"number {n} is {ugly}")
  
checkUgly(6)
checkUgly(1)
checkUgly(14)