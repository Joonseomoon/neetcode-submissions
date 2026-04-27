class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, rr = 0, len(matrix) - 1 

        while rl < rr:
            m = rl + ((rr - rl) // 2)
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                rr = m - 1
            else:
                rl = m + 1

        cl, cr = 0, len(matrix[0]) - 1
        while cl <= cr:
            m = cl + ((cr - cl) // 2)
            if matrix[rl][m] == target:
                return True
            elif matrix[rl][m] > target:
                cr = m - 1
            else:
                cl = m + 1
        return False