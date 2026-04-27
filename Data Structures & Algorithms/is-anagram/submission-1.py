class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        keyS = {}
        keyY = {}
        for x in s:
            if x in key:
                key[x] = key[x] + 1
            else:
                key[x] = 1
        for y in t:
            if y in key:
                key[y] = key[y] + 1
            else:
                key[y] = 1

        return keyS == keyY

        