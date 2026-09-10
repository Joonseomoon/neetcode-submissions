class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        coins.sort()
        dp = [[0 for _ in range(amount + 1)]for _ in range(N + 1)]

        for i in range(N):
            dp[i][0] = 1

        for i in range(N - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a] + dp[i][a - coins[i]]
        return dp[0][amount]
        

