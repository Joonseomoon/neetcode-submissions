class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other = collections.defaultdict()
        for i, n in enumerate(nums):
            if target - n in other:
                return [other[target - n], i]
            other[n] = i