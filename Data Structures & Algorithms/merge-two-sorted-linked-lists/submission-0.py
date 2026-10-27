# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        startAns = ListNode()
        ans = startAns

        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val < p2.val:
                ans.next = p1
                p1 = p1.next
            else:
                ans.next = p2
                p2 = p2.next
            ans = ans.next
        
        # Leftover will all be greater
        if p1: ans.next = p1
        if p2: ans.next = p2

        return startAns.next

