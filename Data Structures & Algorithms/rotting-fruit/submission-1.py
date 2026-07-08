class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        drs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in drs:
                    dr = r + dr
                    dc = c + dc
                    if (dr in range(ROWS) and dc in range(COLS) and grid[dr][dc] == 1):
                        q.append([dr, dc])
                        grid[dr][dc] = 2
                        fresh -= 1
            time += 1
        return time if not fresh else -1