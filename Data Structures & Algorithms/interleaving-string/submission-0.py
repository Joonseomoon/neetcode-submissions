class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i + j >= len(s3):
                return True
            dp[(i, j)] = False
            if i in range(len(s1)) and s3[i + j] == s1[i]:
                dp[(i, j)] = dp[(i, j)] or dfs(i + 1, j)
            if j in range(len(s2)) and s3[i + j] == s2[j]:
                dp[(i, j)] = dp[(i, j)] or dfs(i, j + 1)
            return dp[(i, j)]
        return dfs(0, 0)