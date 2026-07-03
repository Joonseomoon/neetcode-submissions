class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def dfs(r, c):
            nonlocal area
            if (r not in range(ROWS) or 
                c not in range(COLS) or
                grid[r][c] == 0):
                return

            grid[r][c] = 0
            area += 1
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
                    res = max(res, area)
        return res