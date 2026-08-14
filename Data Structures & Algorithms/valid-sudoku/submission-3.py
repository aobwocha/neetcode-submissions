class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sqr = collections.defaultdict(set)

        for row_i in range(9):
            for col_i in range(9):
                cell = board[row_i][col_i]
                if cell == '.': continue

                if cell in row[row_i] or cell in col[col_i] or cell in sqr[(row_i // 3, col_i // 3)]:
                    return False
                
                row[row_i].add(cell)
                col[col_i].add(cell)
                sqr[(row_i // 3, col_i // 3)].add(cell)
        
        return True