class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int) # key -> the num, value -> frequency 
        for n in nums:
            freqs[n] += 1

        res = [0] * k # nums with topKFrequencies
        maxFreqs = [0] * k # max amount frequences found
        for i in range(k):
            for key in freqs:
                if maxFreqs[i] < freqs[key]:
                    res[i] = key
                    maxFreqs[i] = freqs[key]
            freqs.pop(res[i])
        
        return res
