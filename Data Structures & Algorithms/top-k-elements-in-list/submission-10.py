class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} # key: num -> value: count/frequency of num
        buckets = [[] for i in range(len(nums) + 1)] # list of lists with max index of length of nums 

        for n in nums: # build hashmap of frequencies for each unique element
            counts[n] = 1 + counts.get(n, 0)
        
        for n, cnt in counts.items(): # add elements into buckets for each element's respective frequency
            buckets[cnt].append(n)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res