class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        check = [False] * len(nums)

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if check[i]:
                    continue
        
                cur.append(nums[i])
                check[i] = True
                dfs(cur)
                cur.pop()
                check[i] = False
        dfs([])
        return res