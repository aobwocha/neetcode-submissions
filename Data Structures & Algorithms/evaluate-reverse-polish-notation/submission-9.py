class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens:
            try:
                val = int(token)
                stack.append(val)
            except ValueError:
                op = token
                val2 = stack.pop()
                val1 = stack.pop()

                if op == "+":
                    stack.append(val1 + val2)
                elif op == "-":
                    stack.append(val1 - val2)
                elif op == "*":
                    stack.append(val1 * val2)
                elif op == "/":
                    stack.append(int(val1 / val2))
        
        return stack.pop()
