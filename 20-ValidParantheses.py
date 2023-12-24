class Solution:
  def isValid(self, s: str) -> bool:
    stack = deque()
    opens = "({["
    closes = ")}]"
    def match(openB: str, close: str) -> bool:
      # print(f"open: {openB} close: {close}")
      match openB:
        case "(":
          return close == ")"
        case "{":
          return close == "}"
        case "[":
          return close == "]"

    def match2(openB: str, close: str) -> bool:
      idx = opens.index(openB)
      print(idx)
      return openB == closes[idx]

    for c in s:
      if c in opens:
        stack.append(c)
      elif c in closes:
        try:
          if not match(stack.pop(), c):
            return False
        except:
          return False # No item in stack to pop
    return len(stack) == 0

