import heapq
from collections import deque, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Repeatedly grab highest CURRENT frequency that is 
        # available to process. Greedy approach is the answer here
        # because it ensures if other tasks are available that 
        # the idle time that must follow a task is filled with other 
        # tasks instead of idle ticks
        
        # Max-heap of ready tasks
        heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(heap)
        q, t = deque([]), 0
        while q or heap:
            if q and q[0][0] <= t:
                # if ready now put back into candidates
                heapq.heappush(heap, q.popleft()[1])

            if not heap:
                # Nothing ready, time travel
                t = q[0][0]
            else:
                mostFrequentReadyItem = heapq.heappop(heap)
                if mostFrequentReadyItem + 1 < 0:
                    # Not the last of this task
                    q.append((t + n + 1, mostFrequentReadyItem + 1))
                t += 1
        
        return t






        
        