class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i, string in enumerate(strs):
            count = [0] * 26
            for j, s in enumerate(string):
                count[ord(s[j]) - ord('a')] += 1
            if count in groups:
                groups[count] = groups[count] + [i]
            else:
                groups[count] = [i]

        result = []
        for key in groups:
            results += groups[key]
