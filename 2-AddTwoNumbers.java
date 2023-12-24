

class Solution {
  //Definition for singly-linked list.
  public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode a = l1;
        ListNode b = l2;    
        int sum = (a.val + b.val);
        int carry = sum / 10;
        ListNode sumStart = new ListNode(sum % 10);    
        a = a.next;
        b = b.next;
        ListNode sumNode = sumStart;
        int intA;
        int intB;
        
        
        while (carry != 0 || a != null || b != null) {
            intA = 0;
            intB = 0;
            if (a != null) {
                intA = a.val;
                a = a.next;
            }
            if (b != null) {
                intB = b.val;
                b = b.next;
            }
            
            sum = (intA + intB + carry);
            sumNode.next = new ListNode(sum % 10);
            carry = sum / 10;
            sumNode = sumNode.next;
        }
        return sumStart;
    }
}