#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        if not nums or not len(nums):
            return res
        nums.sort()
        for i in range(len(nums)):
            if i%2== 0:
                res+=nums[i]
        return res
# @lc code=end

