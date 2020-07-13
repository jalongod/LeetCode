'''
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0

        dp, i, j = [[0 for _ in range(m)] for __ in range(n)], 0, 0

        while i < m and obstacleGrid[0][i] == 0:
            dp[0][i] = 1
            i += 1
        while j < n and obstacleGrid[j][0] == 0:
            dp[j][0] = 1
            j += 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]


sol = Solution()
res = sol.uniquePathsWithObstacles([[0, 1]])
print(str(res))
