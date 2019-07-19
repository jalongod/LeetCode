'''
51. N皇后
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

'''


class Solution:
    def solveNQueens2(self, n: int):
        res = []
        s = "." * n

        def backtrack(i, tmp, col, sum, minus):
            if i == n:
                res.append(tmp)
                return
            for j in range(n):
                if j not in col and i + j not in sum and i - j not in minus:
                    backtrack(i + 1, tmp + [s[:j] + "Q" + s[j + 1:]],
                              col | {j}, sum | {i + j}, minus | {i - j})

        backtrack(0, [], set(), set(), set())
        return res

    def solveNQueens(self, n: int):
        res = []
        s = "." * n

        def backtrace(i, tmp, col, sum, minus):
            if i == n:
                res.append(tmp)
                return
            for j in range(n):
                if j not in col and i + j not in sum and i - j not in minus:
                    backtrace(i + 1, tmp + [s[:j] + "Q" + s[j + 1:]],
                              col | {j}, sum | {i + j}, minus | {i - j})
                # if valid(i, j, col, sum, minus):
                #     str = s[:j] + ["Q"] + s[j + 1:]
                #     tmp.append(str)
                #     col.append(j)
                #     sum.append(i + j)
                #     minus.append(i - j)
                #     backtrace(tmp, i + 1, col, sum, minus)

        # def valid(i, j, col, sum, minus):
        #     if not col or not sum or not minus:
        #         return True
        #     if col.__contains__(j) or sum.__contains__(
        #             i + j) or minus.__contains__(i - j):
        #         return False
        #     return True
        backtrace(0, [], set(), set(), set())
        # backtrace([], 0, [], [], [])

        return res

    pass


if __name__ == '__main__':
    sol = Solution()
    max = sol.solveNQueens2(4)  # false
    max = sol.solveNQueens(4)  # false
    # max = sol.permuteUnique([1, 2, 3])  # false
    print(max)