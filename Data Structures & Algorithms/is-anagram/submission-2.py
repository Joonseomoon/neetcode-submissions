class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        keyS = {}
        keyY = {}
        for x in s:
            if x in keyS:
                keyS[x] = keyS[x] + 1
            else:
                keyS[x] = 1
        for y in t:
            if y in keyY:
                keyY[y] = keyY[y] + 1
            else:
                keyY[y] = 1

        return keyS == keyY

        