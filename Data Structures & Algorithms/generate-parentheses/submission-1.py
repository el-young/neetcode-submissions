class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, buff = [], []

        def helper(nOpen=0, nClosed=0):
            if nClosed == n:
                ans.append(''.join(buff))
                return
            if nOpen < n:
                buff.append('(')
                helper(nOpen + 1, nClosed)
                buff.pop()
            if nClosed < nOpen:
                buff.append(')')
                helper(nOpen, nClosed + 1)
                buff.pop()

        helper()
        return ans


                    
                    


