class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        
        res = 0
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < nums[r] and nums[m] < nums[l]:
                r = m - 1
                res = nums[m]
            else:
                l = m + 1

        return res