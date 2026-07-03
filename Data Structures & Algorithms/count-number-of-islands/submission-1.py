class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    dr, dc = row + dr, col + dc
                    if (dr in range(ROWS) and
                        dc in range(COLS) and 
                        grid[dr][dc] == "1"):
                        q.append((dr, dc))
                        grid[dr][dc] = "#"
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1

        return res