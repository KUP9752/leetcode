# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def checkSame(root, subRoot) -> bool:
      if not root and not subRoot:
        return True
      if root and subRoot and root.val == subRoot.val:
        return checkSame(root.left, subRoot.left) and checkSame(root.right, subRoot.right)
      return False


    if root and subRoot:
      # if root.val == subRoot.cal:

      return (checkSame(root, subRoot) 
              or self.isSubtree(root.left, subRoot) 
              or self.isSubtree(root.right, subRoot) )
    return False
