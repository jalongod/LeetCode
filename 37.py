'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

'''


class Solution:
    def solveSudoku(self, board) -> None:
        if not board or len(board) == 0:
            return 

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            if valid(board, i, j, str(k)):
                                board[i][j] = str(k)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True

        def valid(b, i, j, v):
            for k in range(9):
                if b[i][k] == v or b[k][j] == v or b[3*int(i / 3) + int(k / 3)][3*int(j / 3) + int(k % 3)] == v:
                    return False
            return True

        solve(board)


if __name__ == '__main__':
    sol = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    max = sol.solveSudoku(board)
    print(max)
