class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, buff = [], []
        def helper(lo=0, currSum=0):
            if currSum > target: return
            if currSum == target:
                ans.append(buff[:])
                return
            
            for i in range(lo, len(nums)):
                buff.append(nums[i])
                helper(i, currSum + nums[i])
                buff.pop()
            
        helper()
        return ans

