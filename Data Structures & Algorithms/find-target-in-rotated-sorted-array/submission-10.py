class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m

            # m in left sorted portion (covers non rotated case)
            if nums[l] <= nums[m]:
                if nums[l] > target or target > nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # m in right sorted portion
            else:
                if nums[m] > target or target > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        