class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + ((r - l) // 2)
            currH = 0 
            for x in piles:
                currH += -(-x // m)
            if currH > h:
                l = m + 1
            else:
                r = m - 1
                res = m
        return res