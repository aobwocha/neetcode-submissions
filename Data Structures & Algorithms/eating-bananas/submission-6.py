class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r
        while l <= r:
            m = (r + l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            
            if hours <= h:
                min_k = min(min_k, m)
                r = m - 1
            else:
                l = m + 1
        
        return min_k