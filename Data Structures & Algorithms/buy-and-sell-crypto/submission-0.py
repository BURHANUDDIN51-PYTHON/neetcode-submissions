from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = 0

        minimum_of_left = prices[0]
        for i in range(1, len(prices)):
            # Calculate profit
            profit = prices[i] - minimum_of_left

           # Maximum
            maximum_profit = max(maximum_profit, profit)
            # Set the minimum of the left side
            minimum_of_left = min(prices[i], minimum_of_left)

        return maximum_profit