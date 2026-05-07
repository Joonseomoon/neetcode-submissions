class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        l, r = 0, 0 # l is beg char of curr substring

        res = 0
        while r < len(s):
            if s[r] in duplicates:
                res = max(res, r - l)
                l = r 
                duplicates = set()
            duplicates.add(s[r])
            r += 1
    
        return res