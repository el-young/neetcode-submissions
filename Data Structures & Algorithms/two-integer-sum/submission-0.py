class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {target - num: idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            if num in m and m[num] != idx:
                return sorted([idx, m[num]])
        