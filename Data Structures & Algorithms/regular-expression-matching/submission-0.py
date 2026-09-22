class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if (i not in range(len(s)) and 
                j not in range(len(p))):
                return True
            if j not in range(len(p)):
                return False
            
            match = (i in range(len(s)) and (s[i] == p[j] or p[j] == "."))
            if (j + 1 in range(len(p)) and p[j + 1] == "*"):
                memo[(i, j)] = (dfs(i, j + 2) or match and dfs(i + 1, j))
                return memo[(i, j)]
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return memo[(i, j)]
        return dfs(0, 0)