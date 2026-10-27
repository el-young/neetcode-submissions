class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_freq, freq = 0, dict()
        start = end = ans = 0
        while end < len(s):
            curr = s[end]
            freq[curr] = freq.get(curr, 0) + 1
            most_freq = max(most_freq, freq[curr])

            if end - start + 1 - most_freq > k:
                freq[s[start]] -= 1
                start += 1
                most_freq = max(freq.values())
    
            ans = max(end - start + 1, ans)
            end += 1
        
        return ans