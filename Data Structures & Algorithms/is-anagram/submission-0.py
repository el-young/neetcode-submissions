class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0] * 26
        freq_t = [0] * 26

        for c in s: freq_s[ord(c) - ord('a')] += 1
        for c in t: freq_t[ord(c) - ord('a')] += 1

        return freq_s == freq_t