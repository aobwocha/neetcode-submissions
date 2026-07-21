class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            rowValues = []
            for num in row:
                if num == '.':
                    continue  
                if num in rowValues:
                    return False    
                rowValues.append(num)
        
        for index in range(len(board)):
            columnValues = []
            for row in board:
                num = row[index]
                if num == '.':
                    continue
                if num in columnValues:
                    return False    
                columnValues.append(num)

        for index in range(0, 9, 3):
            boxValues1 = []
            boxValues2 = []
            boxValues3 = []
            for rowIndex in range(len(board)):
                if rowIndex in range(0, 3): boxValues = boxValues1
                elif rowIndex in range(3, 6): boxValues = boxValues2
                else: boxValues = boxValues3

                for columnIndex in range(index, index+3):
                    num = board[rowIndex][columnIndex]
                    if num == '.':
                        continue 
                    if num in boxValues:
                        return False     
                    boxValues.append(num)
        
        return True

