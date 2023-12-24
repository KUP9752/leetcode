class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # stack = []

    
    n = len(temperatures)
    answer = [0 for _ in range(n)]

    def bruteForce():
      for i, ti in enumerate(temperatures):
        # print(f"i: {i}")
        for j in range(i + 1, n):
          # print(f"j: {j}")
          tj = temperatures[j]
          if (tj > ti):
            answer[i] = j - i
            break
          # print()

    def stack():
      stack = [] #(temp, day)
      for i, ti in enumerate(temperatures):
        while stack and ti > stack[-1][0]:
          tj, j = stack.pop()
          answer[j] = i - j
        stack.append([ti, i])


    stack()
    return answer
