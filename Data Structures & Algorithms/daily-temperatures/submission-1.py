class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((temperatures[i], i))
        return result
            