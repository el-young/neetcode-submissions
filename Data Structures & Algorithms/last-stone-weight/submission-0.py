import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            l1 = -heapq.heappop(heap)
            l2 = -heapq.heappop(heap)
            if l1 != l2:
                heapq.heappush(heap, -(l1 - l2))
        return -heap[0] if heap else 0