class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                prev_i, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (i - prev_i))
                start = prev_i
            
            stack.append((start, height))
        
        while stack:
            prev_i, prev_height = stack.pop()
            max_area = max(max_area, prev_height * (len(heights) - prev_i))
        
        return max_area