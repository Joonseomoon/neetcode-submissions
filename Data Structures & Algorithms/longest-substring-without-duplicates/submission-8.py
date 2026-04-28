class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = {}
        l = 0 # l is beg char of curr substring
        res = 0
        
        for r in range(len(s)):
            if s[r] in duplicates:
                l = max(duplicates[s[r]] + 1, l)
            duplicates[s[r]] = r
            res = max(res, r - l + 1)
        return res