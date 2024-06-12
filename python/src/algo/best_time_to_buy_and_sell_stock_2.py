"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

# Solved with Greedy algorithm

from typing import List

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        start = prices[0]
        n = len(prices)
        for i in range(0 , n):
            if start < prices[i]: 
                profit += prices[i] - start
            start = prices[i]
        return profit
        