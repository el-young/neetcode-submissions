import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            if len(heap) < k:
                # do not have k largest min distances yet
                heapq.heappush(heap, (-dist, point))
            else:
                if dist < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dist, point))
        
        return [point for _, point in heap]