# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node: return (float('inf'), float('-inf'))
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1: return -1
            if left[1] >= node.val: return -1
            if right[0] <= node.val: return -1
            return (min(left[0], node.val), max(right[1], node.val))
        
        return type(dfs(root)) is tuple
