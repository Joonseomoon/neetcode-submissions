class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 if j != len(t) else 1 for j in range(len(t) + 1)]
        for i in range(len(s) - 1, -1 , -1):
            prev = 1
            for j in range(len(t) - 1, -1, -1):
                cur = dp[j]
                if s[i] == t[j]:
                    cur += prev
                prev = dp[j]
                dp[j] = cur
        return dp[0]
