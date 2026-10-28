"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = p = Node(0)
        curr, m = head, dict()
        while curr:
            p.next = Node(curr.val)
            p = p.next
            m[curr] = p
            curr = curr.next
        p.next = None
        
        curr, p = head, dummy.next
        while curr:
            p.random = m.get(curr.random, None)
            curr = curr.next
            p = p.next

        return dummy.next