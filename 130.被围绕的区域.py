#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (38.49%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 46.7K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# 解释:
#
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#

from typing import List


# @lc code=start
class Solution:
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  #上右下左

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(board, node):
            que = []
            que.append(node)
            isLand = True
            memo = []
            while que:
                cur = que.pop(0)
                x, y = cur[0], cur[1]
                board[x][y] = 'N'
                if x >= len(board) - 1 or y >= len(
                        board[0]) - 1 or x <= 0 or y <= 0:
                    isLand = False
                # add to memo
                memo.append(cur)
                for a, b in self.dirs:
                    next_x, next_y = x + a, y + b
                    if next_x < len(board) and next_y < len(
                            board[0]
                    ) and next_x >= 0 and next_y >= 0 and board[next_x][
                            next_y] == "O":
                        que.append([next_x, next_y])
            for n in memo:
                if isLand:
                    board[n[0]][n[1]] = 'X' if isLand else 'N'

        height = len(board)
        if not height:
            return
        width = len(board[0])
        if not width:
            return
        #上边
        for j in range(width):
            if board[0][j] == 'O':
                bfs(board, [0, j])
        #下边
        for j in range(width):
            if board[-1][j] == 'O':
                bfs(board, [-1, j])

        #左边
        for j in range(height):
            if board[0][j] == 'O':
                bfs(board, [0, j])
        #右边
        for j in range(height):
            if board[-1][j] == 'O':
                bfs(board, [-1, j])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'N':
                    board[i][j] = 'O'


# @lc code=end

sol = Solution()
input = []

sol.solve(input)
a = 1
"""
["X","O","O","X","X","X","O","X","O","O"],
["X","X","X","X","X","X","X","X","X","X"],
["X","X","X","X","X","X","X","X","X","X"],
["X","X","X","X","X","X","X","X","X","O"],
["O","X","X","X","X","X","X","X","X","X"],
["X","X","X","X","X","X","X","X","X","X"],
["O","X","X","X","X","X","X","X","X","O"],
["O","X","X","X","X","X","X","X","X","X"],
["X","X","X","X","X","X","X","X","O","O"],
["X","X","X","O","O","X","O","X","X","O"]]

["X","O","O","X","X","X","O","X","O","O"],
["X","O","X","X","X","X","X","X","X","X"],
["X","X","X","X","X","X","X","X","X","X"],
["X","X","X","X","X","X","X","X","X","O"],
["O","X","X","X","X","X","X","X","X","X"],
["X","X","X","X","X","X","X","X","X","X"],
["O","X","X","X","X","X","X","X","X","O"],
["O","X","X","X","X","X","X","X","X","X"],
["X","X","X","X","X","X","X","X","O","O"],
["X","X","X","O","O","X","O","X","X","O"]]
"""