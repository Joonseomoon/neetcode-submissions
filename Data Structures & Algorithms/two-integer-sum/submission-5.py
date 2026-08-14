class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other = collections.defaultdict()
        for i, n in enumerate(nums):
            diff = target - n
            if diff in other:
                return [other[diff], i]
            other[n] = i