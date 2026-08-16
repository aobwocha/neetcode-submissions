class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            min_height = min(heights[left], heights[right])
            curr_area = (right - left) * min_height
            max_area = max(max_area, curr_area)

            if heights[left] == min_height:
                left += 1
            elif heights[right] == min_height:
                right -= 1
        
        return max_area
            
