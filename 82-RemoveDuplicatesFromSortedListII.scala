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
    // var prev: ListNode? 
    // var curr: ListNode?
    val (isHeadRep: Boolean, repStart) = isRepeating(head ?: return null)

    if (isHeadRep) return deleteDuplicates(repStart) 

    val start = head

    var prev = start
    var curr = start
    
    while (curr != null) {
      val (now, new) = removeMultiSequence(prev!!, curr)
      curr = new
      prev = now
    }
    return start
  }
  
  /* takes in current position
   * returns Pair of (if current repeats, the next node after the reps)
   * !does not do the removal
   */
  fun isRepeating(curr: ListNode): Pair<Boolean, ListNode?> {
    var currVal = curr.`val`
    var next: ListNode? = curr.next
    var reps: Boolean = false

    // find if reps
    if (next != null && currVal == next?.`val`) {
      reps = true 
      next = next.next
    }

    // find when it reps until
    while (next != null && currVal == next?.`val`) {
      next = next.next
    }

    return Pair (reps, next)
  }

  fun removeMultiSequence(prev: ListNode, curr: ListNode): Pair<ListNode, ListNode?> {
    var currVal = curr.`val`
    var next: ListNode? = curr.next ?: return Pair(curr, null)
    var reps: Boolean = false
    // null check is for later iterations
    //println("1curr ${curr.`val`} prev ${prev.`val`}")
    while (next != null && curr.`val` == next?.`val`) {
     // println("2curr ${curr.`val`} next ${next.`val`}")
      reps = true
      next = next.next
    }
    var now: ListNode = curr
    if (reps) {
      println("3 prev ${prev.`val`} curr ${curr.`val`}")
      prev.next = next
      now = prev
    }

    return Pair(now, next)
  }
}