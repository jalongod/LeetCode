#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 动态规划


class Solution:
    def maxProduct(self, nums) -> int:
        if nums is None:
            return 0
        dp = [[0 for i in range(2)] for j in range(2)]
        ret, dp[0][0], dp[0][1] = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][0] * nums[i], nums[i])
            ret = max(ret, dp[x][0])
            pass
        return ret


if __name__ == '__main__':
    sol = Solution()
    max = sol.maxProduct([1, 2, 4, 0, 5])
    print(max)
