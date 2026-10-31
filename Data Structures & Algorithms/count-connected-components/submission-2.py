from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor in visited: continue
                dfs(neighbor)
        
        numComp = 0
        for node in adj:
            if node in visited: continue
            dfs(node)
            numComp += 1
        
        # some n may not appear in the adj list (lone nodes)
        return numComp + (n - len(adj))