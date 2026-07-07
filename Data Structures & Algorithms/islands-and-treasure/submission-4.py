class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])

        dist = 1
        drs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in drs:
                    dr = r + dr
                    dc = c + dc
                    if (dr in range(ROWS) and dc in range(COLS) and grid[dr][dc] == (2 ** 31) - 1):
                        q.append([dr, dc])
                        grid[dr][dc] = dist
            dist += 1