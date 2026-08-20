class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = list()
        for i, temp in enumerate(temperatures):          
            while stack and temp > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            
            stack.append((temp, i))
        return result