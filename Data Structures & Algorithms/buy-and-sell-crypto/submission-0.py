class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                temp_profit = price - min_price
                if temp_profit > profit:
                    profit = temp_profit
        
        return profit