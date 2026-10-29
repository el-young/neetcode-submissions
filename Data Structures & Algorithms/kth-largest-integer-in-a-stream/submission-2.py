import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            if self.k > 0:
                heapq.heappush(self.heap, num)
                self.k -= 1
            else:
                if num > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if self.k > 0:
            heapq.heappush(self.heap, val)
            self.k -= 1
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
        

        
