# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def cmp(q1, q2):
            if not q1 and not q2: return True
            if not q1 or not q2 or q1.val != q2.val: return False
            return cmp(q1.left, q2.left) and cmp(q1.right, q2.right)
        
        if not root: return False
        if cmp(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

                 