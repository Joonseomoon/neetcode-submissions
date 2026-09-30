class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        res = []
        while l <= r and t <= b:
            for col in range(l, r + 1):
                res.append(matrix[t][col])
            t += 1

            for row in range(t, b + 1):
                res.append(matrix[row][r])
            r -= 1

            if not (l <= r and t <= b):
                break

            for col in range(r, l - 1, -1):
                res.append(matrix[b][col])
            b -= 1

            for row in range(b, t - 1, -1):
                res.append(matrix[row][l])
            l += 1
        return res