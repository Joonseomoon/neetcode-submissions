class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = {}
            column = {}
            for j in range(9):
                if board[i][j] in hashmap and board[i][j] != ".":
                    return False
                if board[j][i] in hashmap and board[j][i] != ".":
                    return False
                row.add(board[i][j])
                column.add(board[i][j])
        return True