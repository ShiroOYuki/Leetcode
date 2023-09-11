import numpy as np

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        b = list(np.array(board).T)
        for row in 9:
            for i in board[row]:
                if (board[row].count(i) > 1 and ) or b[row].count(i) > 1:
                    return False
        for 

if __name__ == '__main__':
    s = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(s.isValidSudoku(board))