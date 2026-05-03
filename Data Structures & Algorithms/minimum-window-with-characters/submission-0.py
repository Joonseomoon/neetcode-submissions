class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        countRef = collections.defaultdict(int)
        countWin = collections.defaultdict(int)

        for c in t:
            countRef[c] += 1
        
        have = 0
        need = len(countRef)
        l = 0
        minLen = float("inf")
        res = ""


        for r in range(l, len(s)):
            countWin[s[r]] += 1 

            if s[r] in countRef and countWin[s[r]] == countRef[s[r]]:
                have += 1

            
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    res = s[l:r + 1]

                countWin[s[l]] -= 1
                if s[l] in countRef and countWin[s[l]] < countRef[s[l]]:
                    have -= 1
                l += 1

        return res
            