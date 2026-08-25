class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, n in enumerate(s):
            lastIndex[n] = i

        res = []
        size = 0
        end = -1

        for i in range(len(s)):
            size += 1
            end = max(end, lastIndex[s[i]])

            if end == i:
                res.append(size)
                size = 0 

        return res