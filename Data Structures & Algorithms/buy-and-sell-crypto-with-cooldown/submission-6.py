class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1, buy2, sell = 0, 0, 0
        for i in range(n - 1, -1, -1):
            temp = buy1
            buy1 = max(sell - prices[i], buy1)
            sell = max(buy2 + prices[i], sell)
            buy2 = temp

        return buy1