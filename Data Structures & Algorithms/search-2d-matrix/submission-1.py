class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right_row = len(matrix) - 1
        left_row = 0

        while left_row <= right_row:
            row_idx = (right_row + left_row) // 2
            right = len(matrix[row_idx]) - 1
            left = 0

            while left <= right:
                mid = (right + left) // 2
                if matrix[row_idx][mid] == target:
                    return True
                if matrix[row_idx][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            if matrix[row_idx][0] < target < matrix[row_idx][-1]:
                return False
            
            if right == -1:
                right_row = row_idx - 1
            else:
                left_row = row_idx + 1
        
        return False