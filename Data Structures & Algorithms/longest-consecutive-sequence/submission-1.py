class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        res = 1
        for n in nums:
            if n-1 in hashmap:
                hashmap[n] = hashmap[n-1] + 1
                if hashmap[n] > res:
                    res = hashmap[n]
            else:
                hashmap[n] = 1
        return res