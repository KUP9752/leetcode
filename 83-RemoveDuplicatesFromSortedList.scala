/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
  fun deleteDuplicates(head: ListNode?): ListNode? {
    val start: ListNode = head ?: return null
    var curr: ListNode? = start
    while (curr != null) {
      curr = removeDuplicateSequence(curr)   
    }
    return start
  }
  
  /* removes the duplicates of the given value
   * returns the next *different* node
   */
  fun removeDuplicateSequence(curr: ListNode): ListNode? {
    var currVal = curr.`val`
    var next: ListNode? = curr.next ?: return null
    while (next != null && curr.`val` == next?.`val`) {
      println(s"curr ${curr.`val`} next ${next.`val`}")
      next = next.next
    }

    curr.next = next
    return next
  }
}