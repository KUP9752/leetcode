# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  maxDia = 0
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    

    def crawl(root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      
      lH = crawl(root.left)
      rH = crawl(root.right)
      
      self.maxDia = max(self.maxDia, lH + rH)
      return 1 + max(lH, rH)
      


    crawl(root)
    return self.maxDia
        