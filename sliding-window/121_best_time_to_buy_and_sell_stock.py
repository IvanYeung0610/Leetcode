"""
Ivan Yeung

121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # iterate through list and get two pointers
        # one pointers moves forward while the other stays on the smallest value
        least = 0
        cursor = 0
        max_profit = 0
        while cursor < len(prices):
            max_profit = max((prices[cursor] - prices[least]), max_profit)
            # shift the least pointer if the cursor is indexing a smaller value
            if (prices[cursor] < prices[least]):
                least = cursor
            cursor += 1

        return max_profit
