class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = nums[0]
        for n in nums[1:]:
            curMax = max(n, n + curMax)
            res = max(res, curMax)
        return res