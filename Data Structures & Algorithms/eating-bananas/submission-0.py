class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)
        res = -1
        while minK <= maxK:
            m = minK + ((maxK - minK) // 2)
            currH = 0 
            for x in piles:
                currH += -(-x // m)
            if currH > h:
                minK = m + 1
            else:
                maxK = m - 1
                res = m
        return res