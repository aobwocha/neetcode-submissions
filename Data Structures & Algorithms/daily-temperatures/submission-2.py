class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            counter = 0
            while stack and temp > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            
            stack.append((temp, i))
        
        return result