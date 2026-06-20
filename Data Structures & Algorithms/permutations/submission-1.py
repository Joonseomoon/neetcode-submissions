class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, check):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if check[i]:
                    continue
        
                cur.append(nums[i])
                check[i] = True

                dfs(cur, check)

                cur.pop()
                check[i] = False
        dfs([], [False] * len(nums))
        return res