class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i, string in enumerate(strs):
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            count = tuple(count)
            if count in groups:
                groups[count] = groups[count] + [i]
            else:
                groups[count] = [i]

        result = []
        for key in groups:
            result.append(groups[key])
        return result