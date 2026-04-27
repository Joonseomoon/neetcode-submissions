class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while minK <= maxK:
            m = l + ((r - l) // 2)
            currH = 0 
            for x in piles:
                currH += -(-x // m)
            if currH > h:
                minK = m + 1
            else:
                maxK = m - 1
                res = m
        return res