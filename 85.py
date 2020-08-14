'''
85. 最大矩形
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
动态规划
dp[i][j]    以i，j为右下角的最大的矩形的面积
dp[0][0]==1 if m[0][0]=='1' else 0
[1:][1:]
    dp[i][j]=
'''


class Solution:
    def largestRectangleArea(self, h) -> int:
        if len(h) == 0:
            return 0
        min_index = h.index(min(h))
        leftLarge = self.largestRectangleArea(h[:min_index])
        midLarge = h[min_index] * len(h)
        rightLarge = self.largestRectangleArea(h[min_index + 1:])
        return max(leftLarge, midLarge, rightLarge)

    def maximalRectangle(self, m) -> int:
        if not m:
            return 0
        height, width = len(m), len(m[0])
        val = [[0 for _ in range(width)] for __ in range(height)]
        res = 0
        for j in range(width):
            for i in range(height):
                cur_val = 0 if m[i][j] == '0' else 1
                if i == 0 or cur_val == 0:
                    val[i][j] = cur_val
                else:
                    val[i][j] = val[i - 1][j] + cur_val
        for i in range(len(val)):
            res = max(res, self.largestRectangleArea(val[i]))
        return res


sol = Solution()
res = sol.maximalRectangle([["0", "1"], ["1", "0"]])

# res = sol.maximalRectangle([["1", "0", "1", "0",
#                              "0"], ["1", "0", "1", "1", "1"],
#                             ["1", "1", "1", "1", "1"],
#                             ["1", "0", "0", "1", "0"]])
print(str(res))
