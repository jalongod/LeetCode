#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 动态规划
# 300. 最长上升子序列


class Solution:
    def lengthOfLIS(self, nums) -> int:
        length = len(nums)
        if length <= 0:
            return 0
        mlen = 1
        ret = [1] * len(nums)
        for i in range(1, len(nums)):
            ret[i] = 1
            for j in range(0, i):
                if (nums[j] < nums[i]):
                    ret[i] = max(ret[i], ret[j] + 1)
            mlen = max(mlen, ret[i])
        return mlen


if __name__ == '__main__':
    sol = Solution()
    max = sol.lengthOfLIS([0])
    # max = sol.lengthOfLIS([2, 5, 3, 7])
    print(max)
