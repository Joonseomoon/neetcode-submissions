class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            column = set()
            if i % 3 == 0:
                box1 = set()
                box2 = set()
                box3 = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row:
                    return False
                if board[j][i] != "." and board[j][i] in column:
                    return False
                if board[i][j] != "." and 0 <= j <= 2 and board[i][j] in box1:
                    return False
                if board[i][j] != "." and 3 <= j <= 5 and board[i][j] in box2:
                    return False
                if board[i][j] != "." and 6 <= j <= 8 and board[i][j] in box3:
                    return False
                row.add(board[i][j])
                column.add(board[j][i])
                if 0 <= j <= 2:
                    box1.add(board[i][j])
                if 3 <= j <= 5:
                    box2.add(board[i][j])
                if 6 <= j <= 8:
                    box3.add(board[i][j])
        return True