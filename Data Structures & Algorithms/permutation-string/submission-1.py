class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = dict()
        for c in s1: freq[c] = freq.get(c, 0) + 1
        
        start, end = 0, 0
        while end < len(s2):
            if end < len(s1):
                if s2[end] in freq: freq[s2[end]] -= 1
                if all(map(lambda x: x == 0, freq.values())): return True
            else:
                if s2[start] in freq: freq[s2[start]] += 1
                if s2[end] in freq: freq[s2[end]] -= 1
                if all(map(lambda x: x == 0, freq.values())): return True
                start += 1
            end += 1
        
        return False
