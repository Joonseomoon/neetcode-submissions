class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 if j != len(t) else 1 for j in range(len(t) + 1)]
        
        for i in range(len(s) - 1, -1 , -1):
            nextDp = [0 if j != len(t) else 1 for j in range(len(t) + 1)]
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    nextDp[j] = dp[j] + dp[j + 1]
                else:
                    nextDp[j] = dp[j]
            dp = nextDp
        return dp[0]
