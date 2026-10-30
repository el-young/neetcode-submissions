class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, buff, seen = [], [], set()
        def helper():
            if len(buff) >= len(nums):
                ans.append(buff[:])
                return

            for i in range(len(nums)):
                if i in seen: continue
                buff.append(nums[i])
                seen.add(i)
                helper()
                seen.remove(i)
                buff.pop()
        helper()
        return ans