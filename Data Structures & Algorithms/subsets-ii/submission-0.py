class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, buff = [], []
        def helper(lo=0):
            ans.append(buff[:])
            
            for i in range(lo, len(nums)):
                # Generating all subsets for [1,1,1,2,5]
                # with 1 (index 0) as the start fully encapsulates
                # generate all subsets for [1,1,1,2,5] with 1 (index 1) as
                # as the start, we can prune these search spaces.
                # i == lo means this duplicate 1 is a result of the parents
                # restriction which means we are building the longest subsets
                # still.
                if i > lo and nums[i] == nums[i - 1]: continue
                buff.append(nums[i])
                helper(i + 1)
                buff.pop()
        
        helper()
        return ans