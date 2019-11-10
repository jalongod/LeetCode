#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (24.32%)
# Likes:    1505
# Dislikes: 0
# Total Accepted:    115.8K
# Total Submissions: 474.8K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#

# 思路
# 1 暴力 i,j,k
# 2 i,j hash 容易覆盖重复元素，暂不考虑
# 3 夹逼：先排序 i<0返回结果 从i+1到n-1中查找，如果三者的和大于0，移动右指针，否则移动左指针

from typing import List


# @lc code=start
class Solution:
    # 1.暴力 time exceed
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums.sort()
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             for k in range(j + 1, len((nums))):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     thr = []
    #                     thr.append(nums[i])
    #                     thr.append(nums[j])
    #                     thr.append(nums[k])
    #                     thr.sort()
    #                     if thr not in res:
    #                         res.append(thr)
    #     return res

    # 3. i,j,hash
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums.sort()
        res, length, i = [], len(nums), 0
        while nums[i] <= 0 and i < length - 2:
            j, k, u = i + 1, length - 1, {}
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            while j < k:
                if nums[j] in u:
                    j += 1
                    continue
                if nums[k] in u:
                    k -= 1
                    continue
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    u.setdefault(nums[j])
                    u.setdefault(nums[k])
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
            i += 1

        return res


# @lc code=end

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
