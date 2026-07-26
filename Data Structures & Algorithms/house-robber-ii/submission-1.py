class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            one, two = 0, 0
            for n in nums:
                temp = two
                two = max(one + n, two)
                one = temp
            return two

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))