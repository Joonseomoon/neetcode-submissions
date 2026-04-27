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
        for c in s:
            if count == -1:
                count = int(c)
            else: 
                string += c
                count -= 1
                if count == 0:
                    res += string[1:]
                    string == ""
            
