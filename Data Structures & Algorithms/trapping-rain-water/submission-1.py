class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = height[0]
        r_max = height[-1]
        result = 0

        l = 1
        r = len(height) - 2

        while l <= r:
            if l_max <= r_max:
                result += max(l_max - height[l], 0)
                l_max = max(l_max, height[l])
                l += 1
            else:
                result += max(r_max - height[r], 0)
                r_max = max(r_max, height[r])
                r -= 1
        
        return result