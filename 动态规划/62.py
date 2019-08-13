'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
动态规划
dp定义 dp[i][j] 为从i，j点到终点的路径总数
初始值 dp[m][n],dp[m-1][n],dp[m][n-1]=0,1,1
dp公式 dp[m][n]=dp[m+1][n]+dp[m][n+1]
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m <= 1 or n <= 1:
            return 1
        dp = [[0 for _ in range(m)] for __ in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for j in range(n):
            dp[j][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]


sol = Solution()
res = sol.uniquePaths(7, 3)
print(str(res))
