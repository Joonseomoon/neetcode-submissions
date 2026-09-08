class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            buy = dp[i + 1][False] - prices[i]
            cooldown = dp[i + 1][True] 
            dp[i][True] = max(buy, cooldown)

            sell = dp[i + 2][True] + prices[i]
            cooldown = dp[i + 1][False]
            dp[i][False] = max(sell, cooldown)

        return dp[0][1] 