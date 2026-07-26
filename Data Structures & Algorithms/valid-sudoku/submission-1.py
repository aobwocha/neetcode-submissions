class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row_idx in range(9): 
            for col_idx in range(9):
                if board[row_idx][col_idx] == ".": continue

                if (board[row_idx][col_idx] in cols[col_idx] or
                    board[row_idx][col_idx] in rows[row_idx] or
                    board[row_idx][col_idx] in squares[(row_idx // 3, col_idx // 3)]
                ): return False

                cols[col_idx].add(board[row_idx][col_idx])
                rows[row_idx].add(board[row_idx][col_idx])
                squares[(row_idx // 3, col_idx // 3)].add(board[row_idx][col_idx])
        
        return True