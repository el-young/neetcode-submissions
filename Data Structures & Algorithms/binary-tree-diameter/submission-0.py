# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0
        def dfs(node):
            nonlocal maxDiam

            depthL = depthR = 0
            if node.left: depthL = 1 + dfs(node.left)
            if node.right: depthR = 1 + dfs(node.right)

            maxDiam = max(maxDiam, depthL + depthR)
            return max(depthL, depthR)
        
        dfs(root)
        return maxDiam
            
            
