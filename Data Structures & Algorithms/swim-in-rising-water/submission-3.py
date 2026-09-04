class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minHeap:
            cur, r, c = heapq.heappop(minHeap)
            if (r == N - 1 and c == N - 1):
                return cur

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR in range(N) and neiC in range(N) and 
                    (neiR, neiC) not in visited):
                    visited.add((neiR, neiC))
                    heapq.heappush(minHeap, (max(cur, grid[neiR][neiC]), neiR, neiC))
