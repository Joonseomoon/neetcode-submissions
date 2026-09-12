class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        
        dp = [False for _ in range(len(s2) + 1)]
        dp[len(s2)] = True

        for i in range(len(s1), -1, -1):
            nextDp = [False for _ in range(len(s2) + 1)]
            if i == len(s1):
                nextDp[len(s2)] = True
            for j in range(len(s2), -1, -1):
                if i in range(len(s1)) and s3[i + j] == s1[i] and dp[j]:
                    nextDp[j] = True
                if j in range(len(s2)) and s3[i + j] == s2[j] and nextDp[j + 1]:
                    nextDp[j] = True
            dp = nextDp
        return dp[0]