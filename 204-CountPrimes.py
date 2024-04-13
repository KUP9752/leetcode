import math

class Solution:
  # Number of primes strictly less than (<) n
  def countPrimes(self, n: int) -> int:
    if n <= 1:
      return 0
    
    ## count non-primes then find the primes
    primes = [True for _ in range(n)]
    
    
    primes[0] = False  # 1 is not prime
    primes[1] = False  # 2 is prime
    count = 1 # count non-primes
    
    for i in range(2, int(math.sqrt(n)) + 1):
      if primes[i]:
        for j in range(i * i, n, i):
          if primes[j]:
            count += 1
          primes[j] = False
        
    return n - count - 1 # -1 as n is not included
  
sol = Solution()

print(f"{sol.countPrimes(0) = }")
print(f"{sol.countPrimes(10) = }")