class Solution:
  def maxProfit(self, prices: List[int]) -> int:

    left = 0
    right = left
    
    currMax = 0
    while right < len(prices):

      if prices[right] > prices[left]:
        profit = prices[right] - prices[left]
        currMax = max(currMax, profit)
      else:
        left = right

      right += 1
    return currMax
