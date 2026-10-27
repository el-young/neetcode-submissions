# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        while n > 0: 
            fast = fast.next
            n -= 1

        prev = None
        while fast: 
            prev, slow, fast = slow, slow.next, fast.next
        
        if prev is None: return head.next

        prev.next = slow.next
        return head
