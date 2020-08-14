#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
from typing import List
class Solution:
    #前缀法 子序和
    #超时
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     preSum = [0 for _ in range(len(nums)+1)]
    #     sum = 0
    #     for i in range(len(nums)):
    #         sum+=nums[i]
    #         preSum[i+1] = sum
    #     for i in range(1,len(preSum)):
    #         for j in range(i):
    #             if preSum[i]-preSum[j] == k:
    #                 res+=1
    #     return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        preSum = {}
        sum = 0
        preSum.setdefault(0,1)
        for num in nums:
            sum += num
            if preSum.__contains__(sum-k):
                res+=preSum[sum-k]
            if preSum.__contains__(sum):
                preSum[sum] = preSum.get(sum)+1
            else:
                preSum[sum] = 1
        return res
# @lc code=end

sol = Solution()
res = sol.subarraySum([1,1,1],2)
print(res)