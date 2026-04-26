class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        indexStack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(temp)
                indexStack.append(i)
            else:
                while stack[-1] < temp:
                    result[indexStack[-1]] = i - indexStack[-1] 
                    stack.pop()
                    indexStack.pop()
                    if not stack:
                        break
                stack.append(temp)
                indexStack.append(i)
        return result