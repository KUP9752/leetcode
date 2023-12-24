/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def hasPathSum(root: TreeNode, targetSum: Int): Boolean = {
      def climber(curr: TreeNode, acc: Int): Boolean = {
        //short circuit if the branch doesn't exist
        if (curr == null) return false

        val newAcc = acc + curr.value
        
        (curr.left, curr.right) match {
          // leaf reached
          case (null, null) => newAcc == targetSum
          // only left child
          // case (left, null) =>
          // // only right child
          // case (null, right) =>
          // irrespective of whether right or left as long as either exists
          case (left, right) => climber(left, newAcc) || climber(right, newAcc)
        }
      }
        //does shortcircuiting explore useless paths and waste memory by doing a return false?
      def climber2(curr: TreeNode, acc: Int): Boolean = {
        // if (curr == null) {
        //   println("hello") 
        //   return false
        //   }
        val newAcc = acc + curr.value
      
        (curr.left, curr.right) match {
          // leaf reached
          case (null, null) => newAcc == targetSum
          // only left child
          case (left, null) => climber(left, newAcc)
          // only right child
          case (null, right) => climber(right, newAcc)
          // both exists
          case (left, right) => climber(left, newAcc) || climber(right, newAcc)
        }   
      }
      root match {
        //empty list
        case null => false
        case _    => climber2(root, 0)
      }
    }
}