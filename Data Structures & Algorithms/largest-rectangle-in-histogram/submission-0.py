class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                start = index
                maxArea = max((i - index) * height, maxArea)
            stack.append([start, h])

        for i, h in stack:
            maxArea = max((len(heights) - i) * h, maxArea)
        return maxArea