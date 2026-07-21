class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        matching_cases = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for bracket in s:
            if bracket in matching_cases.values():
                stack.append(bracket)
            elif not stack or matching_cases[bracket] != stack.pop():
                return False
        
        return stack == []