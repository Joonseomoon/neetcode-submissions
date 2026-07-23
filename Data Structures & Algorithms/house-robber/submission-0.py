class Solution:
    def rob(self, nums: List[int]) -> int:
        m1, m2 = 0, 0
        for n in nums:
            temp = max(n + m2, m1)
            m2 = m1
            m1 = temp

        return m1
