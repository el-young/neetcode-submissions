# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        def inOrder(root, k):
            if not root: return k, None
            k, ans = inOrder(root.left, k)
            if ans is not None: return k, ans
            k -= 1
            if k == 0: return k, root.val
            return inOrder(root.right, k)
        
        return inOrder(root, k)[1]