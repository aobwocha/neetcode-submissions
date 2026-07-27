class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            min_h = min(heights[left], heights[right])
            area = (right - left) * min_h
            res = max(area, res)

            if min_h == heights[left]:
                left += 1
            else:
                right -= 1
        
        return res