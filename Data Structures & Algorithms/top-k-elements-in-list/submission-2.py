class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums: freq[num] = freq.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq.items(): buckets[freq].append(num)
        
        ans = []
        for bucket in reversed(buckets):
            if bucket:
                ans.extend(bucket)
                k -= len(bucket)
            
            if k <= 0:
                return ans
        

