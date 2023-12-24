# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      def crawl(root: Optional[TreeNode], h: int) -> int:
        if not root:
          return h

        leftH = crawl(root.left, h + 1)
        rightH = crawl(root.right, h + 1)

        return max(leftH, rightH)
      return crawl(root, 0)