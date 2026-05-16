class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        count = [0] * n 
        for x in nums:
            if count[x - 1] > 0:
                return x
            count[x - 1] += 1
        