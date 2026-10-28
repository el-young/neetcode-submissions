# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        prevDepth, buff, ans = 0, [], []
        q = [(root, 0)]
        while q:
            node, depth = q.pop(0)

            if prevDepth != depth: 
                ans.append(buff.copy())
                buff.clear()

            buff.append(node.val)
            prevDepth = depth
            
            if node.left: q.append((node.left, depth + 1))
            if node.right: q.append((node.right, depth + 1))

        ans.append(buff)
        return ans


