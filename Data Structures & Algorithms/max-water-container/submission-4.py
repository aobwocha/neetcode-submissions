class Solution:
    def maxArea(self, heights: List[int]) -> int:
        LEFT, RIGHT = 0, len(heights) - 1
        max_water = 0

        while LEFT < RIGHT:
            if heights[LEFT] <= heights[RIGHT]:
                max_water = max(max_water, heights[LEFT] * (RIGHT - LEFT))
                LEFT += 1
            else:
                max_water = max(max_water, heights[RIGHT] * (RIGHT - LEFT))
                RIGHT -= 1
        
        return max_water