class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixP = 1
        prefixes = [1] * len(nums)
        for i in range(len(nums)):
            prefixes[i] = prefixP
            prefixP *= nums[i]

        suffixP = 1
        suffixes = [1] * len(nums)
        for j in range(len(nums) - 1, -1, -1):
            suffixes[j] = suffixP
            suffixP *= nums[j]

        res = [1] * len(nums)
        for k in range(len(nums)):
            res[k] = prefixes[k] * suffixes[k]
        return res