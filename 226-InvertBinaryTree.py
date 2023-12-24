# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # if not root:
    #   return root ##returns None

    # newLeft = self.invertTree(root.right)
    # newRight = self.invertTree(root.left)
    # return TreeNode(val=root.val, left=newLeft, right=newRight)
        
    # modify in place?

    if not root:
      return root #returns None

    self.invertTree(root.left) #in place modificiaton
    self.invertTree(root.right) #in plcae modification

    root.left, root.right = root.right, root.left

    return root
