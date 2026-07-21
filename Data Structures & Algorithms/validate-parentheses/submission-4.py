class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            elif stack:
                if bracket == ')' and stack.pop() != '(':
                    return False
                
                if bracket == '}' and stack.pop() != '{':
                    return False
                
                if bracket == ']' and stack.pop() != '[':
                    return False
            else:
                return False
        
        return not stack

        