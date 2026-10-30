class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, buff = [], []
        def helper(lo=0):
            for lo in range(lo, len(nums)):
                buff.append(nums[lo])
                helper(lo + 1)
                buff.pop()
            ans.append(buff[:])
        helper()
        return ans