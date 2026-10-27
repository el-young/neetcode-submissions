class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, profit = prices[0], 0
        for price in prices:
            if price < start:
                start = price
            else:
                profit = max(profit, price - start)
            
        return profit
            