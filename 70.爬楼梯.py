#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (47.08%)
# Likes:    692
# Dislikes: 0
# Total Accepted:    98.8K
# Total Submissions: 209.7K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#
#

# 找重复子问题


# @lc code=start
class Solution:
    # dp
    # def climbStairs(self, n: int) -> int:
    #     if n <= 2:
    #         return n
    #     dp = [0 for _ in range(n + 1)]
    #     dp[1] = 1
    #     dp[2] = 2
    #     for i in range(3, n + 1):
    #         dp[i] = dp[i - 1] + dp[i - 2]
    #     return dp[n]

    # dp 优化
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(n - 2):
            b, a = a + b, b
        return b


# @lc code=end

sol = Solution()
res = sol.climbStairs(5)
print(res)
