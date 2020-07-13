#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.20%)
# Likes:    642
# Dislikes: 0
# Total Accepted:    100.9K
# Total Submissions: 195.8K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#、、、、、
#
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#
#

from typing import List

# @lc code=start
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = sys.maxsize
        # res = 0
        # for i in range(len(prices)):
        #     if buy > prices[i]:
        #         buy = prices[i]
        #     else:
        #         res = max(res, prices[i] - buy)
        # return res

        # dp dp[i]在i节点卖出能获取的最大利润
        # 这样的话，dp[i]与dp[i-1]无法建立连接
        # dp[i][1]在节点之前买入能获取的最大利润
        # dp[i][0]在节点之前卖出能获取的最大利润
        # dp[0][0] = 0
        # dp[0][1] = 0

        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[0]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(-prices[i], dp[i - 1][1])
        return dp[n - 1][0]


# @lc code=end
