class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        res = 0
        minHeap = [(0, 0)]
        visit = set()

        while len(visit) < N:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
                
            visit.add(node)
            res += cost
            x1, y1 = points[node]
            for nei, (x2, y2) in enumerate(points):
                if nei not in visit and node != nei:
                    neiCost = abs(x2 - x1) + abs(y2 - y1)
                    heapq.heappush(minHeap, (neiCost, nei))
        return res