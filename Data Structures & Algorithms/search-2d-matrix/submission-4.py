class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        TOP, BOT = 0, len(matrix) - 1
        while TOP <= BOT:
            MID = (TOP + BOT) // 2
            if matrix[MID][0] > target:
                BOT = MID - 1
            elif matrix[MID][-1] < target:
                TOP = MID + 1
            else:
                break
        
        if TOP > BOT:
            return False
        
        ROW = (TOP + BOT) // 2
        LEFT, RIGHT = 0, len(matrix[ROW]) - 1
        while LEFT <= RIGHT:
            MID = (RIGHT + LEFT) // 2
            if matrix[ROW][MID] == target:
                return True
            elif matrix[ROW][MID] > target:
                RIGHT = MID - 1
            else:
                LEFT = MID + 1
        
        return False