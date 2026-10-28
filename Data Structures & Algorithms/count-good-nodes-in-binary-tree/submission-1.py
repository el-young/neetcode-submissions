# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currMax=-100):
            if not root: return 0
            ans = root.val >= currMax
            ans += dfs(root.left, max(root.val, currMax))
            ans += dfs(root.right, max(root.val, currMax))
            return ans
        return dfs(root)

