class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = 0

        for r in range(len(nums)):
            # maintain monotonic decreasing queue
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(r)

            # only start appending to output when window size becomes valid of k size
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res
