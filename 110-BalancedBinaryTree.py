# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      return self.crawl(root)[0]

    def crawl(self, root: Optional[TreeNode]) -> (bool, int):
      if not root:
        return True, 0
        
      isL, lH = self.crawl(root.left)
      isR, rH = self.crawl(root.right)
      
      return isL and isR and abs(lH - rH) <= 1, max(lH, rH) + 1
      
        