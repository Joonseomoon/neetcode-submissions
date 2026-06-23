class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(open, close):
            if len(stack) == 2 * n:
                res.append("".join(stack))
                return
            
            if close < open:
                stack.append(")")
                dfs(open, close + 1)
                stack.pop()
            
            if open < n:
                stack.append("(")
                dfs(open + 1, close)
                stack.pop()
        dfs(0, 0)
        return res