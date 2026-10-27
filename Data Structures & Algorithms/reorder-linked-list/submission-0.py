# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle node
        mid = curr = head
        while curr and curr.next:
            mid = mid.next
            curr = curr.next.next
        
        # Reverse after mid
        prev, curr = None, mid.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Construct answer, prev is head of reversed list
        p1, p2 = head, prev
        while p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        mid.next = None
        

            