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
            
        generatedBrackets = []
        generation(generatedBrackets, '', 0, 0, n)
        return generatedBrackets
        
        

            
            