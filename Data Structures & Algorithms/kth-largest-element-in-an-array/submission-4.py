import heapq, random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heapify-Grab-K method
        # time: O(n + klogn), space: O(n)
        # heap = [-num for num in nums]
        # heapq.heapify(heap)
        # while k > 1: 
        #     heapq.heappop(heap)
        #     k -= 1
        # return -heapq.heappop(heap)
        
        # Top-K method
        # time: O(nlogk) space: O(k)
        # heap = []
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap, num)
        #     else:
        #         if num > heap[0]:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap, num)
        # return heapq.heappop(heap)

        # Quickselect

        # def partition(arr, lo, hi):
        #     pivot = lo
        #     i = j = lo + 1
        #     while j <= hi:
        #         if arr[j] < arr[pivot]:
        #             # Swap to < pivot frontier
        #             arr[i], arr[j] = arr[j], arr[i]
        #             i += 1
        #         j += 1

        #     arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
        #     return i - 1
        
        # # The index target, partition will return the index
        # # of the item in its sorted position so for kth largest
        # # we want the index len(nums) - k
        # target = len(nums) - k
        # lo, hi = 0, len(nums) - 1
        # while True:
        #     pivot = random.randint(lo, hi)
        #     # Swap to front, our partition code assumes this
        #     nums[pivot], nums[lo] = nums[lo], nums[pivot]
        #     sortedIndex = partition(nums, lo, hi)
        #     if sortedIndex == target: return nums[sortedIndex]
        #     elif sortedIndex < target: lo = sortedIndex + 1
        #     else: hi = sortedIndex - 1

        # Quickselect with 3-way partition

        def threeWayPartition(arr, lo, hi):
            pivot = lo
            i = j = lo + 1
            while j <= hi:
                if arr[j] < arr[pivot]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                j += 1
            
            arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
            startEqual = i - 1
            
            # Second pass but now from startEqual + 1 to hi
            j = i
            while j <= hi:
                if arr[i] == arr[startEqual]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                j += 1
            
            return (startEqual, i - 1)
        
        target = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while True:
            pivot = random.randint(lo, hi)
            # Swap to front, our partition code assumes this
            nums[pivot], nums[lo] = nums[lo], nums[pivot]
            startEqual, endEqual = threeWayPartition(nums, lo, hi)
            if startEqual <= target <= endEqual: return nums[startEqual]
            elif startEqual < target: lo = endEqual + 1
            else: hi = startEqual - 1


