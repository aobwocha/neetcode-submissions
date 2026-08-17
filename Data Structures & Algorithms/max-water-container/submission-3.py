class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            curr_area = r - l
            if heights[l] < heights[r]:
                curr_area *= heights[l]
                l += 1
            else:
                curr_area *= heights[r]
                r -= 1
            
            max_area = max(max_area, curr_area)
        
        return max_area