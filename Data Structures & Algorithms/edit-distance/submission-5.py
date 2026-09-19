class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            n, m = m, n
            word1, word2 = word2, word1
        dp = [0 for _ in range(n + 1)]
        nextDp = [0 for _ in range(n + 1)]

        for j in range(n + 1):
            dp[j] = n - j
        
        for i in range(len(word1) - 1, -1, -1):
            nextDp[n] = m - i
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    nextDp[j] = dp[j + 1]
                else:
                    nextDp[j] = 1 + min(dp[j], nextDp[j + 1], dp[j + 1])
            dp = nextDp[:]
        return dp[0]