from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # If numEdges < n - 1 some node must not be reached
        if len(times) < n - 1: return -1

        adj = defaultdict(list)
        for a, b, t in times: adj[a].append((b, t))

        dist = defaultdict()
        heap = [(0, k)]
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist: continue
            dist[node] = d
            for neighbor, w in adj[node]: heapq.heappush(heap, (d + w, neighbor))
        
        return max(dist.values()) if len(dist) == n else -1



