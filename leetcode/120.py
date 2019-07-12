class Solution:

    # dp
    def minimumTotal1(self, triangle) -> int:
        if not triangle or not triangle[0]:
            return 0
        return self._dp(triangle)

    def _dp(self, triangle):
        # 状态定义  dp[i][j],到达i行，j列的时候的最短路径
        # 初始值  第n-1行为本身
        # 状态推倒
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])

        # 最优解
        return triangle[0][0]
        pass

    minLen = float('inf')

    # 深度递归
    def minimumTotal(self, triangle) -> int:
        if not triangle or not triangle[0]:
            return 0
        self._dfs(triangle, 0, 0, "", 0)
        return self.minLen

    def _dfs(self, triangle, i, j, path, length):
        # recursion terminator
        if i == len(triangle) - 1:
            path += str(triangle[i][j]) + '#'
            length += triangle[i][j]
            print(path + str(length))
            self.minLen = length if self.minLen == float('inf') else min(
                self.minLen, length)
            return
        # process logic
        path += str(triangle[i][j]) + '->'
        length += triangle[i][j]
        # deep in
        self._dfs(triangle, i + 1, j, path, length)
        self._dfs(triangle, i + 1, j + 1, path, length)
        # reset state
        # no need to reset
        pass


if __name__ == '__main__':
    sol = Solution()
    max = sol.minimumTotal([[-1], [3, 2], [1, -2, -1]])
    print(max)
