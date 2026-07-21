class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            minHeight = min(heights[left], heights[right])
            area =  minHeight * abs(right-left)
            result = max(area, result)
            if minHeight ==  heights[left]:
                left += 1
            else:
                right -= 1
        return result
