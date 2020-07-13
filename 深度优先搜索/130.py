class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # i j
        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        if row < 3 or col < 3:
            return

        def dfs(i, j):
            if i < 0 or i > row - 1 or j < 0 or j > col - 1:
                return
            if board[i][j] != 'O':
                return
            board[i][j] = '#'
            for d in dir:
                dfs(i + d[0], j + d[1])

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for j in range(col):
            dfs(0, j)
            dfs(row - 1, j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        A = 0


if __name__ == '__main__':
    # board = [
    #     ['X', 'X', 'X', 'X'],
    #     ['X', 'O', 'O', 'X'],
    #     ['X', 'X', 'O', 'X'],
    #     ['X', 'O', 'X', 'X'],
    # ]
    board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    sol = Solution()
    max = sol.solve(board)
    print(max)
