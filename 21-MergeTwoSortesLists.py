# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummyHead = ListNode() #head will come next 

    curr1 = list1
    curr2 = list2
    prev = dummyHead
    while curr1 and curr2:
      if curr1.val <= curr2.val:
        prev.next = curr1
        prev = curr1
        curr1 = curr1.next
      else:
        prev.next = curr2
        prev = curr2
        curr2 = curr2.next
    if curr1: ## curr2 == None
      prev.next = curr1
    if curr2: ## curr1 == None
      prev.next = curr2
    
    return dummyHead.next



