class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        max_hist = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                prev_i, prev_height = stack.pop()
                max_hist = max(max_hist, (i - prev_i) * prev_height)
                start = prev_i
            
            stack.append((start, height))
        
        while stack:
            prev_i, prev_height = stack.pop()
            max_hist = max(max_hist, (len(heights) - prev_i) * prev_height)

        return max_hist