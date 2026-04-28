class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        l, r = 0, 0 # l is beg char of curr substring

        res = 0
        while r < len(s):
            if s[r] in duplicates:
                res = max(res, r - l)
                while l < r and s[l] != s[r]:
                    duplicates.remove(s[l])
                    l += 1
                l += 1
            duplicates.add(s[r])
            r += 1
    
        return max(res, r - l)