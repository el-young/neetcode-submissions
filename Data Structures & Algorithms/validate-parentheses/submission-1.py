class Solution:
    def isValid(self, s: str) -> bool:
        m = {'{': '}', '[': ']', '(': ')'}
        stack = []

        for c in s:
            if c in m:
                stack.append(c)
            else:
                if not stack or m[stack[-1]] != c:
                    return False
                stack.pop()
        
        return len(stack) == 0