class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        TOP, BOTTOM = 0, len(matrix) - 1

        while TOP <= BOTTOM:
            MID = (BOTTOM + TOP) // 2
            if target < matrix[MID][0]:
                BOTTOM = MID - 1
            elif target > matrix[MID][-1]:
                TOP = MID + 1
            else:
                break
        
        if TOP > BOTTOM: 
            return False
        
        ROW = (BOTTOM + TOP) // 2
        LEFT, RIGHT = 0, len(matrix[ROW]) - 1

        while LEFT <= RIGHT:
            MID = (RIGHT + LEFT) // 2
            if target == matrix[ROW][MID]:
                return True
            elif target > matrix[ROW][MID]:
                LEFT = MID + 1
            else:
                RIGHT = MID - 1
        
        return False