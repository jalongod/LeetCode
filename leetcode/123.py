#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 动态规划
# 买卖股票的最佳时机  最多交易两次

import numpy as np


class Solution:
    def maxProfit(self, prices, times=2) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices is None:
            return 0
        res, length = 0, len(prices)
        if length == 0:
            return 0
        mp = [[[0] * 2 for _ in range(2)] for _ in range(length)]
        for i in range(1, length):
            for j in range(times - 1, -1, -1):
                # if i == 1:
                mp[0][j][0] = mp[i][0][0] = 0
                mp[0][j][1] = -prices[0]
                mp[i][0][1] = -float('Inf')

                mp[i][j][0] = max(mp[i - 1][j][0], mp[i - 1][j][1] + prices[i])
                mp[i][j][1] = max(mp[i - 1][j][1],
                                  mp[i - 1][j - 1][0] - prices[i])
            print('第' + str(i + 1) + '天:' + str(mp[i][times - 1][0]))
        return mp[length - 1][times - 1][0]


if __name__ == '__main__':
    sol = Solution()
    max = sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4, 3, 4, 3, 4])
    print(max)
