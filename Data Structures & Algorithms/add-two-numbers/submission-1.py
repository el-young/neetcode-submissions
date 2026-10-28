# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = curr = ListNode()
        carry, p1, p2 = 0, l1, l2
        while p1 or p2 or carry:
            summ = p1.val if p1 else 0
            summ += p2.val if p2 else 0
            summ += carry
            curr.next = ListNode(summ % 10)
            carry = summ >= 10
            curr = curr.next
            if p1: p1 = p1.next
            if p2: p2 = p2.next
        return d.next