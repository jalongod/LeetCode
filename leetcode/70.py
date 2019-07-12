#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 动态规划


class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 0):
            return 0
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [2 for i in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 3]

    def climbStairs3(self, n: int) -> int:
        x, y = 1, 2
        for i in range(n - 2):
            temp = x
            x = y
            y = temp + y
        return y

    def climbStairs4(self, n: int) -> int:
        x, y = 0, 1
        for _ in range(n):
            x, y = y, x + y
        return y


if __name__ == '__main__':
    sol = Solution()
    max = sol.climbStairs4(5)
    print(max)
