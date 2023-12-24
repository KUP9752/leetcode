class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    res = []
    temp = []
    def go(opens: int, closes: int):
      if opens == closes == n:
        res.append("".join(temp))
        return
      if (opens < n):
        temp.append("(")
        go(opens + 1, closes)
        temp.pop()
      if closes < opens:
        temp.append(")")
        go(opens, closes + 1)
        temp.pop()

        
    go(0, 0)
    return res