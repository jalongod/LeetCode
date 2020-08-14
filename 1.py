'''
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    # def twoSum(self, nums, target):
    #     lens = len(nums)
    #     j = -1
    #     for i in range(1, lens):
    #         temp = nums[:i]
    #         if (target - nums[i]) in temp:
    #             j = temp.index(target - nums[i])
    #             break
    #     if j >= 0:
    #         return [j, i]

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            area = nums[:i]
            if (target - nums[i]) in area:
                j = area.index(target - nums[i])
                break
        return [j, i]


sol = Solution()
# max = sol.twoSum([2, 7, 11, 15], 9)
max = sol.twoSum([2, 5, 5, 11], 10)
print(max)
max = sol.twoSum([3, 2, 4], 6)
print(max)
