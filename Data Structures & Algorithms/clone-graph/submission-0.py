class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        m = dict()
        def dfs(node):
            copy = Node(node.val)
            m[node] = copy
            for neighbor in node.neighbors:
                # Copy was already created by some other pointer
                if neighbor in m:
                    copy.neighbors.append(m[neighbor])
                else:
                    copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)