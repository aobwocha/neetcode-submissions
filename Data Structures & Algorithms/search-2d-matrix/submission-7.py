class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        TOP, BOTTOM = 0, len(matrix) - 1
        while TOP <= BOTTOM:
            ROW = (BOTTOM + TOP) // 2
            if matrix[ROW][0] <= target <= matrix[ROW][-1]:
                break
            elif matrix[ROW][0] > target:
                BOTTOM = ROW - 1
            else:
                TOP = ROW + 1
        
        if TOP > BOTTOM:
            return False
        
        ROW = (BOTTOM + TOP) // 2
        l, r = 0, len(matrix[ROW]) - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[ROW][m] == target:
                return True
            elif matrix[ROW][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False