class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(List) # key: frequency tuple set ---> value: list of strings
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord("a")] += 1
            res[tuple(counts)].append(s)
        return list(res.values())