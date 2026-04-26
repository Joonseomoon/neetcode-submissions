class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
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
                    if count == 0:
                        res.append("")
                        count = -1
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