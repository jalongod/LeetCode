#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.23%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    37.8K
# Total Submissions: 87.1K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#

# 动态规划
# 定义dp
# dp[i] 最后一个元素为List[i]的最长子序列的长度
# dp[0] = 1

from typing import List


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# @lc code=end

sol = Solution()
sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
