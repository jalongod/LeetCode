#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (58.89%)
# Likes:    892
# Dislikes: 0
# Total Accepted:    99.7K
# Total Submissions: 168.2K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
# 示例:
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
#
#
from typing import List
# @lc code=start

# 方法有：
# 1.O(n^2)枚举 x y
# 2.O(n) 左右边界往中间夹逼


class Solution:
    # 暴力，i j
    # time exceed
    # def maxArea(self, height: List[int]) -> int:
    #     res = 0
    #     for i in range(0, len(height)-1):
    #         for j in range(i+1, len(height)):
    #             rl = (j-i)*min(height[i], height[j])
    #             res = max(res, rl)
    #     return res

    # 左右往中间逼近
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            minHeight = 0
            if height[i] < height[j]:
                minHeight = height[i]
                i += 1
            else:
                minHeight = height[j]
                j -= 1
            area = minHeight * (j - i + 1)
            res = max(res, area)
        return res


# @lc code=end

sol = Solution()
sol.maxArea()
