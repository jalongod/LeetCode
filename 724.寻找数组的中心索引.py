#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#
from typing import List
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = -1
        preSum = [0 for _ in range(len(nums)+1)]
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            preSum[i+1] = sum
        for i in range(len(nums)):
            if preSum[i]==(preSum[-1]-nums[i])/2:
                res = i
                break
        return res
# @lc code=end

sol = Solution()
print(sol.pivotIndex([-1,-1,-1,0,1,1]))

