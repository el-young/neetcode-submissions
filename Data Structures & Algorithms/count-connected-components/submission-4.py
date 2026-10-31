from collections import deque
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
        def bfs(start):
            visited.add(start)
            q = deque([start])
            while q:
                node = q.popleft()
                for n in adj[node]:
                    if n in visited: continue
                    visited.add(n)
                    q.append(n)
        
        components = 0
        for n in adj:
            if n in visited: continue
            bfs(n)
            components += 1

        return components