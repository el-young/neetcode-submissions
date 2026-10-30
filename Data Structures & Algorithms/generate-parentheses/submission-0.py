class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, buff = [], []
        def helper(nOpen=0, nClosed=0, bal=0):

            # Ensured only valid builds
            if nOpen + nClosed >= 2*n:
                ans.append(''.join(buff))
                return
            
            if bal <= 0:
                # Equal closed and opens, can not be an
                # answer, base case already cleared that
                # we must have more opens to use.
                buff.append('(')
                helper(nOpen + 1, nClosed, bal + 1)
                buff.pop()
            else:
                # More open than closed, can add more opens
                # if not beyond n or start closing

                if nOpen < n:
                    buff.append('(')
                    helper(nOpen + 1, nClosed, bal + 1)
                    buff.pop()
                
                buff.append(')')
                helper(nOpen, nClosed + 1, bal - 1)
                buff.pop()
        
        helper()
        return ans


                    
                    


