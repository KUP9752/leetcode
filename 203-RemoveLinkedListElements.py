# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head:
      # Checks if the first node needs to be removed
      if head.val == val: head = head.next
      # leave loop if we have found the head node
      else: break 
      
    curr = head
    while curr:
      if curr.next and curr.next.val == val: curr.next = curr.next.next
      # Skip when the item is to be kept
      else: curr = curr.next
    return head
      
      
    