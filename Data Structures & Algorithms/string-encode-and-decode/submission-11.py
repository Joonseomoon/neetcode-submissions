class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            currlen = len(string)
            res += str(currlen) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        count = -1
        countS = ""
        string = ""

        for c in s:
            if count == -1:
                if c == "#":
                    count = int(countS)
                    countS = ""
                else:
                    countS += c
            else:
                string += c
                count -= 1
                if count == 0:
                    res.append(string)
                    string = ""
                    count = -1

        return res