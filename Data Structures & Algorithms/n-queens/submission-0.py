class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(row_idx):
            if row_idx == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for col_idx in range(n):
                if (col_idx in col or
                    (row_idx + col_idx) in posDiag or
                    (row_idx - col_idx) in negDiag):
                    continue
            
                col.add(col_idx)
                posDiag.add(row_idx + col_idx)
                negDiag.add(row_idx - col_idx)
                board[row_idx][col_idx] = "Q"

                dfs(row_idx + 1)

                col.remove(col_idx)
                posDiag.remove(row_idx + col_idx)
                negDiag.remove(row_idx - col_idx)
                board[row_idx][col_idx] = "."
        
        dfs(0)
        return res
