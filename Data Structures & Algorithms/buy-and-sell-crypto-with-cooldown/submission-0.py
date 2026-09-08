class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key = (i, buying); value = maxProfit

        def dfs(i, buying):
            if i not in range(len(prices)):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                cur = dfs(i + 1, not buying) - prices[i]
            else:
                cur = dfs(i + 2, not buying) + prices[i]

            cooldown = dfs(i + 1, buying)
            dp[(i, buying)] = max(cooldown, cur)
            return dp[(i, buying)]

        return dfs(0, True)
