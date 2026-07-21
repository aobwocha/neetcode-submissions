class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        def generation(generatedBrackets, currentBracket, opened, closed, n):
            if len(currentBracket) == 2 * n:
                generatedBrackets.append(currentBracket)
                return
            
            if opened < n:
                generation(generatedBrackets, currentBracket + '(', opened+1, closed, n)
            
            if closed < opened:
                generation(generatedBrackets, currentBracket + ')', opened, closed+1, n)
            
        
        def validParenthesis(brackets) -> bool:
            stack = []
            for bracket in brackets:
                if bracket == '(':
                    stack.append(bracket)
                elif stack:
                    stack.pop()
                else:
                    return False
            return (len(stack) == 0)

        generatedBrackets = []
        generation(generatedBrackets, '', 0, 0, n)
        result = []
        for bracket in generatedBrackets:
            if validParenthesis(bracket):
                result.append(bracket)
        return generatedBrackets

        
        

            
            