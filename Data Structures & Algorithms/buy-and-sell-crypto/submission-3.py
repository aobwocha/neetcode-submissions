class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price > min_price:
                max_profit = max(max_profit, price - min_price)
            else:
                min_price = price
        
        return max_profit