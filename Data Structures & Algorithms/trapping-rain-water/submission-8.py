class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max = 0, 0
        l, r = 0, len(height) - 1
        total = 0

        while l <= r:
            if l_max <= r_max:
                total += max(l_max - height[l], 0)
                l_max = max(l_max, height[l])
                l += 1
            else:
                total += max(r_max - height[r], 0)
                r_max = max(r_max, height[r])
                r -= 1
        
        return total