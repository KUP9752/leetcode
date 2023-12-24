# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    leftStack = []
    rightStack = []
    
    ## find middle, which will be the end of the list
    left = head
    right = head
    while right: ## if right is not over the list
      if not right.next: ## if right is at the end of the list no more checking
        break
      left = left.next
      leftStack.append(left) ## exlcudes head in the stack
      right = right.next.next ## 2 increments in right

    ## middle is found, this is the final in chain.
    end = left
    leftStack = leftStack[::-1] ##reverse the stack

    ## append to right stack excluding mid, 
    left = left.next ##one after middle
    while left:
      rightStack.append(left)
      left = left.next

    # print(f"ls : {leftStack}")
    # print(f"rs : {rightStack}")
    # print()

    ## either left and right Stack are equal length or right is one shorter (odd or even intial len)
    curr = head
    while leftStack and rightStack:
      curr.next = rightStack.pop()
      curr.next.next = leftStack.pop()
      curr = curr.next.next

    while leftStack: ##should at max be one item
      curr.next = leftStack.pop()
    
    end.next = None ##set the final one to point to nothing

    ### Could be done in place, by reversing the second half of list




        