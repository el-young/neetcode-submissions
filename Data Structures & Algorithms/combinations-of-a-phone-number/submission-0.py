class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans, buff = [], []
        def helper(i=0):
            if i >= len(digits): 
                ans.append("".join(buff))
                return
            for option in m[digits[i]]:
                buff.append(option)
                helper(i + 1)
                buff.pop()
        
        helper()
        return ans