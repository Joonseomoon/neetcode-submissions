class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for i in range(N):
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if a >= coins[i] else 0
        return dp[amount]