class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = 0
        min_value = prices[0]
        max_profit = 0

        for i, val in enumerate(prices):
            profit = val - min_value

            if profit > max_profit:
                max_profit = profit

            if val < min_value:
                min_index = i
                min_value = val
        
        return max_profit
        