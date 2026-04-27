class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l1, l2, r = 0, 1, len(nums) - 1
        res = set()

        while l1 <= len(nums) - 3:
            while r > l2:
                if (nums[l1] == nums[l2] or
                    nums[l1] == nums[r] or
                    nums[l2] == nums[r]):
                    r -= 1
                elif nums[l1] + nums[l2] + nums[r] == 0:
                    triplet = [nums[l1], nums[l2], nums[r]]
                    res.add(tuple(triplet))
                    r -= 1
            r = len(nums) - 1
            if l2 > l1 and l2 < r - 1:
                l2 += 1
            else: 
                l1 += 1
                l2 = l1 + 1
        
        return [list(triplet) for triplet in res]


                