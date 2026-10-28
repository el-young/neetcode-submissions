# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors, path = dict(), []
        
        def dfs(node):
            if not node or len(ancestors) == 2: return
            if node == p or node == q: ancestors[node] = path[:] + [node]
            path.append(node)
            dfs(node.left)
            dfs(node.right)
            path.pop()
        
        dfs(root)

        minn, i = min(len(ancestors[p]), len(ancestors[q])), 0
        while i < minn and ancestors[q][i] == ancestors[p][i]: i += 1
        return ancestors[p][i - 1]

            
            

            
