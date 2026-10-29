import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = [-num for num in nums]
        # heapq.heapify(heap)
        # while k > 1: 
        #     heapq.heappop(heap)
        #     k -= 1
        # return -heapq.heappop(heap)
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heapq.heappop(heap)
