class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_i, prev_temp = stack.pop() 
                result[prev_i] = i - prev_i
            
            stack.append((i, temp))

        return result