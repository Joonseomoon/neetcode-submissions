class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixP = 1
        prefixes = []
        for i in range(len(nums)):
            prefixes[i] = prefixP
            prefixP *= nums[i]
        suffixP = 1
        suffixes = []
        for j in range(len(nums) - 1, 0, -1):
            suffixes[j] = suffixP
            suffixP *= nums[j]
        res = []
        for k in range(len(nums)):
            res[k] = prefixes[k] * suffixes[k]
        return res