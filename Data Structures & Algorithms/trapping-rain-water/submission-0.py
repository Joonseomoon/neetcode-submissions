class Solution:
    def trap(self, height: List[int]) -> int:
        p1, p2 = 0, 1
        area = 0
        while p1 != len(height) - 1:
            if height[p1] > 1:
                while height[p2] < height[p1]:
                    p2 += 1
                    if p2 == len(height) - 1:
                        break
                
                length = p2 - p1 - 1
                currHeight = min(height[p1], height[p2])
                diff = 0
                check = True
                if p2 == len(height) - 1 and height[p2] < height[p1]:
                    check = False
                while p1 < p2 - 1:
                    p1 += 1
                    diff += height[p1]
                if check:
                    area += (length * currHeight) - diff
            p1 += 1 
            p2 += 1

        return area