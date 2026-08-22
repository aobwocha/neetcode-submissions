class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        max_area = 0
        for i, height in enumerate(heights):           
            initial_i = i
            while stack and height < stack[-1][1]:
                prev_i, prev_height = stack.pop()
                curr_area = prev_height * (i - prev_i) 
                max_area = max(curr_area, max_area)
                initial_i = prev_i
            
            stack.append((initial_i, height))
        
        while stack:
            prev_i, prev_height = stack.pop()
            curr_area = prev_height * (len(heights) - prev_i) 
            max_area = max(curr_area, max_area)
        
        return max_area

            
