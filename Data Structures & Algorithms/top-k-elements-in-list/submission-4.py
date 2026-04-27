class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1

        res = [0] * k
        for i in range(k):
            for key in freqs:
                if res[i] < freqs[key]:
                    res[i] = key
        
        return res
