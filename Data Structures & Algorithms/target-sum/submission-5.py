class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = collections.defaultdict(int)
        dp[0] = 1

        for i in range(n):
            nextDp = collections.defaultdict(int)
            for total, count in dp.items():
                nextDp[total + nums[i]] += count
                nextDp[total - nums[i]] += count
            dp = nextDp
        return dp[target]