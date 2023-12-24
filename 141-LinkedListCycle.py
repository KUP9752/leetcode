# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    
    if head and head.next:
      slow = head
      fast = head.next.next
    else:
      return False

    
    while fast != slow:
      if fast and fast.next:
        fast = fast.next.next
      else:
        return False
      slow = slow.next
    
    return True