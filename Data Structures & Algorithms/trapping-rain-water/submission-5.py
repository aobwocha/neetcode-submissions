class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = 0
        r_max = 0
        total = 0

        LEFT, RIGHT = 0, len(height) - 1
        while LEFT <= RIGHT:
            if l_max <= r_max:
                total += max(l_max - height[LEFT], 0)
                l_max = max(l_max, height[LEFT])
                LEFT += 1
            else:
                total += max(r_max - height[RIGHT], 0)
                r_max = max(r_max, height[RIGHT])
                RIGHT -= 1
        
        return total