#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1,len(nums)):
            dp[i] = nums[i] + max(dp[i-1],0)
        return max(dp)
# @lc code=end

