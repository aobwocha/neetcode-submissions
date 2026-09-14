class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = list()
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                prev_i, prev_height = stack.pop()
                max_area = max(max_area, (i - prev_i) * prev_height)
                start = prev_i
            
            stack.append((start, height))
        
        for i, height in stack:
            max_area = max(max_area, (len(heights) - i) * height)
        
        return max_area