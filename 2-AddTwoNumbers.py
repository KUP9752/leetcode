# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    curr1 = l1
    curr2 = l2
    carry = 0
    tot = 0
    dummyHead = ListNode()
    newCurr = dummyHead
    while curr1 or curr2:
      tot += carry
      if curr1:
        tot += curr1.val
        curr1 = curr1.next
      if curr2:
        tot += curr2.val
        curr2 = curr2.next
      carry = tot // 10
      tot = tot % 10

      newCurr.next = ListNode(tot)
      newCurr = newCurr.next
      tot = 0
    
    if carry > 0:
      newCurr.next = ListNode(carry)
      newCurr = newCurr.next

    return dummyHead.next

