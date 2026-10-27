class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_strs = sorted([(sorted(s), idx) for idx, s in enumerate(strs)])
        
        ans, group = [], []
        prev = s_strs[0][0]
        for s, idx in s_strs:
            if s == prev:
                group.append(strs[idx])
            else:
                ans.append(group[:])
                group = [strs[idx]]
                prev = s

        ans.append(group)
        return ans