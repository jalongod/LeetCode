'''
698. 划分为k个相等的子集
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 1 1 1 2 2 3 3 3 4  5

import types


class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        val = sum(nums)/k
        if not isinstance(val, int):
            return False
        nums.sort(reverse=True)
        for i in nums:
            if nums[i] > val:
                return False
            elif nums[i] == val:
                nums.pop(i)

        def match(nums, val):
            if len(nums) == 0:
                return True
            if match(nums[-1], val) or match():
                pass
            
            pass
        pass        


sol = Solution()
max = sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
print(max)
