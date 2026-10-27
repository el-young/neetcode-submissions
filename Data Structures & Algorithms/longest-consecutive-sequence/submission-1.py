class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        digits = set(nums)
        
        starts = []
        for num in nums:
            if num - 1 not in digits:
                starts.append(num)
        
        max_length = 0
        for start in starts:
            length, curr = 1, start
            while curr + 1 in digits:
                curr += 1
                length += 1
            max_length = max(max_length, length)
        
        return max_length
