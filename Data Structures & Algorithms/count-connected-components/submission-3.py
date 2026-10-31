from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = range(n)
        # May be lone nodes (no edges in or out) make sure these
        # are in the adj list
        adj = {node: [] for node in nodes}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node):
            visited.add(node)
            for nxt in adj[node]:
                if nxt not in visited:
                    dfs(nxt)

        components = 0
        for node in adj:
            if node not in visited:
                dfs(node)
                components += 1
        return components