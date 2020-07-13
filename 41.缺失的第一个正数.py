#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
from typing import List 
# @lc code=start
import sys
#思想：把nums[i]放在i处，遍历i处不为i的即为结果。如果1-n齐全，判断nums[0]即可。


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 1
        for i in range(n):
            if nums[i]>0 and nums[i]<n and nums[i]!=nums[nums[i]]:
                a = nums[i]
                b = nums[nums[i]]
                nums[i]=b
                nums[nums[i]]=a
        for i in range(1,n):  
            if nums[i]!=i:
                return i
        if nums[0] == n:
            return n+1
        return n
        

# @lc code=end

sol = Solution()
res = sol.firstMissingPositive([1,2,0]);
print(res)

