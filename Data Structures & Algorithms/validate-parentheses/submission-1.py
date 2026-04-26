class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {"]":"[", "}":"{", ")":"("}
        for x in s:
            if x in closed:
                if not stack:
                    return False
                curr = stack.pop()
                if curr != closed[x]:
                    return False
            else:
                stack.append(x)
        
        return not stack