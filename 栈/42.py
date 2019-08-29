#!/usr/bin/python3
'''
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# class Solution:  # dp 解法 dp[i][0]第i列的左边的最高  dp[i][1]第i列的右边的最高
#     def trap(self, height) -> int:
#         res = 0
#         leng = len(height)
#         dp = [[0] * 2 for _ in range(leng)]
#         for i in range(1, leng):
#             dp[i][0] = max(dp[i - 1][0], height[i - 1])

#         for i in range(leng - 2, -1, -1):
#             dp[i][1] = max(dp[i + 1][1], height[i + 1])
#         for i in range(leng):
#             min_height = min(dp[i][0], dp[i][1])
#             if min_height > height[i]:
#                 res = res + (min_height - height[i])
#         return res


class Solution:  # 栈解法
    def trap(self, height) -> int:
        res, cur, leng = 0, 0, len(height)
        stack = []
        while cur < leng:
            while len(stack) > 0 and height[cur] > height[stack[len(stack) -
                                                                1]]:
                h = height[stack[len(stack) - 1]]
                stack.pop()
                if len(stack) <= 0:
                    break
                distance = cur - stack[len(stack) - 1] - 1  # 两堵墙之前的距离。
                min_height = min(height[stack[len(stack) - 1]], height[cur])
                res = res + distance * (min_height - h)
            stack.append(cur)
            cur += 1
        return res


sol = Solution()
max = sol.trap([])
print(max)
