class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = ans = 0
        seen = dict()

        while end < len(s):
            nxt = s[end]
            if nxt in seen and seen[nxt] >= start:
                ans = max(ans, end - start)
                start = seen[nxt] + 1
            seen[nxt] = end
            end += 1
    
        return max(ans, end - start)

            