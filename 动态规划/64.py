'''
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
动态规划
dp[i][j] 从0,0到i,j的最短路径和
dp横竖为初始值
dp[i][j] = min(dp[i-1][j],dp[i][j-1])
'''


class Solution:
    def minPathSum(self, grid) -> int:
        height, width = len(grid), len(grid[0])
        if height == width and height == 0:
            return 0
        dp = [[0 for _ in range(width)] for __ in range(height)]
        dp[0][0] = grid[0][0]
        for i in range(height):
            for j in range(width):
                if i == 0 and j == 0:
                    continue
                if i < 1:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j < 1:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[height - 1][width - 1]


sol = Solution()
res = sol.minPathSum([[1, 1]])
print(str(res))
