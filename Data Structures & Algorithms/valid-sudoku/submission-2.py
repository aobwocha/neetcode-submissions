class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row_idx in range(9):
            for col_idx in range(9):
                cell = board[row_idx][col_idx]

                if cell == ".": continue
                
                if (cell in rows[row_idx] or
                    cell in cols[col_idx] or
                    cell in squares[(row_idx // 3, col_idx // 3)]
                ): return False

                rows[row_idx].add(cell)
                cols[col_idx].add(cell)
                squares[(row_idx // 3, col_idx // 3)].add(cell)
        
        return True