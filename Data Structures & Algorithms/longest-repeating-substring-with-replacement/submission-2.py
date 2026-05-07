class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = collections.defaultdict(int)
        maxF = 0
        res = 0 

        for r in range(len(s)):
            count[s[r]] += 1
            maxF = max(maxF, count[s[r]])
            while (r - l + 1) - maxF > k:
                l += 1
            res = max(res, r - l + 1)
        return res
