class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        LEFT = 1
        RIGHT = max(piles)
        min_k = RIGHT

        while LEFT <= RIGHT:
            k = (RIGHT + LEFT) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours > h:
                LEFT = k + 1
            else:
                min_k = min(min_k, k)
                RIGHT = k - 1
            
        return min_k