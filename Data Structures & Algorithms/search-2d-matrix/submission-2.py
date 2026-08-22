class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_r = 0
        r_r = len(matrix) - 1
        t_r = None
        while l_r <= r_r:
            m_r = (r_r + l_r) // 2
            
            if matrix[m_r][0] <= target <= matrix[m_r][-1]:
                t_r = m_r
                break
            
            if matrix[m_r][0] > target:
                r_r = m_r - 1
            else:
                l_r = m_r + 1
        
        l = 0
        r = len(matrix[m_r]) - 1
        while l <= r:
            m = (r + l) // 2

            if matrix[m_r][m] == target:
                return True
            elif matrix[m_r][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False
        
