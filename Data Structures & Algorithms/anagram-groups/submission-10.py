class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            count = tuple(count)
            if count in groups:
                groups[count] = groups[count] + [string]
            else:
                groups[count] = [string]

        result = []
        for key in groups:
            result.append(groups[key])
        return result