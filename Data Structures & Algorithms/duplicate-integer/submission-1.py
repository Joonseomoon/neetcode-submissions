class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()
        for x in nums:
            if x in track:
                return True
            track.add(x)
        return False