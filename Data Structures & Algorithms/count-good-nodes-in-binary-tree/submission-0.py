# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxs, ans = [], 0

        def dfs(root):
            nonlocal ans
            if not root: return

            if not maxs or root.val >= maxs[-1]:
                ans += 1
                maxs.append(root.val)
            else:
                maxs.append(maxs[-1])

            dfs(root.left)
            dfs(root.right)
            maxs.pop()
        
        dfs(root)
        return ans

