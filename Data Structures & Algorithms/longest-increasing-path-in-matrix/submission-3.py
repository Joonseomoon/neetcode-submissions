class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, prev):
            if (r not in range(ROWS) or 
                c not in range(COLS) or 
                matrix[r][c] <= prev):
                return 0
            if dp[r][c] != -1:
                return dp[r][c]

            dp[r][c] = 1 + max(dfs(r + 1, c, matrix[r][c]), dfs(r - 1, c, matrix[r][c]), dfs(r, c + 1, matrix[r][c]), dfs(r, c - 1, matrix[r][c]))
            return dp[r][c]

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if dp[r][c] == -1:
                    res = max(res, dfs(r, c, -1))
        return res
                