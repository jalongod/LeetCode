#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 动态规划
# 买卖股票的最佳时机


class Solution:
    def maxProfit(self, prices) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices is None:
            return 0
        res, length = 0, len(prices)
        if length == 0:
            return 0
        mp = [[0 for i in range(2)] for j in range(length)]
        mp[0][0], mp[0][1] = 0, -prices[0]
        for i in range(1, length):
            mp[i][0] = max(mp[i - 1][0], mp[i - 1][1] + prices[i])
            mp[i][1] = max(mp[i - 1][1], mp[i - 1][0] - prices[i])
            res = max(res, mp[i][0], mp[i][1])
            pass
        return res


if __name__ == '__main__':
    sol = Solution()
    max = sol.maxProfit([7, 1, 5, 3, 6, 4])
    print(max)
