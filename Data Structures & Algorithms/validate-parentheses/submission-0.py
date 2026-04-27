class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {"]":"[", "}":"{", ")":"("}
        for x in s:
            if x in closed:
                curr = stack.pop()
                if curr != closed[x]:
                    return False
            else:
                stack.append(x)
        
        return not stack