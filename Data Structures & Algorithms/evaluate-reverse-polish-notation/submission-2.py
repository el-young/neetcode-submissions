class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in {"-", "+", "*", "/"}:
                stack.append(int(tok))
            else:
                r, l = stack.pop(), stack.pop()
                if tok == "+":
                    stack.append(l + r)
                elif tok == "*":
                    stack.append(l * r)
                elif tok == "-":
                    stack.append(l - r)
                else:
                    stack.append(int(l / r))

        return stack[0]


