class CountSquares:

    def __init__(self):
        self.pointCounts = collections.defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointCounts[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        diags = []
        for x, y in self.points:
            if ((x, y) != (qx, qy) and 
                abs(qx - x) == abs(qy - y)):
                diags.append([x, y])
        
        res = 0
        for x, y in diags:
            if ((qx, y) in self.pointCounts and 
                (x, qy) in self.pointCounts):
                res += self.pointCounts[(qx, y)] * self.pointCounts[(x, qy)]
        return res

