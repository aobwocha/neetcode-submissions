class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        res = []

        def backtracking(i, path):
            open_count, closed_count = 0, 0
            for bracket in path:
                open_count += 1 if bracket == "(" else 0
                closed_count += 1 if bracket == ")" else 0

            if i == (2 * n): 
                if open_count == closed_count:
                    res.append(path)
                return
                        
            backtracking(i + 1, path + "(")
            if open_count > closed_count:
                backtracking(i + 1, path + ")")
            
        backtracking(0, "")
        return res

