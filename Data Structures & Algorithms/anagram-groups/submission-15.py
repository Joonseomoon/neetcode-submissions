class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # key: frequency tuple set ---> value: list of strings

        counts = [0] * 26
        for s in strs:
            for c in s:
                counts[ord(c) - ord("a")] += 1
            if tuple(counts) in hashmap:
                hashmap[tuple(counts)] += [s]
            else:
                hashmap[tuple(counts)] = [s]
        
        res = []
        for key in hashmap:
            res += hashmap[tuple(counts)]
        return res
        