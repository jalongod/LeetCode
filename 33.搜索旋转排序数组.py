#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.09%)
# Likes:    408
# Dislikes: 0
# Total Accepted:    54.1K
# Total Submissions: 149.4K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
#

# 看到O(log n) 就想到二分查找

# 思路1 遍历数组，找到最大值 O(n)，从左侧查找或者从右侧查找O(log n )

# 思路2  如果target<mid而且target>left 从左侧查找 else 从右侧查找
# 如果 target <right
#        if target == mid return
#        else if target>mid or mid>right 从右侧查找
#           else 从左侧查找
#     else
#        if target == mid return
#        if target<mid or mid<right 从右侧
#           else 从左侧查找

from typing import List


# @lc code=start
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + int((right - left) >> 1)
    #         if target == nums[mid]:
    #             return mid
    #         if nums[left] <= nums[mid]:  # 前半部分有序
    #             if target >= nums[left] and target < nums[mid]:  # 左侧
    #                 right = mid - 1
    #             else:  # 右侧
    #                 left = mid + 1
    #         else:
    #             if target <= nums[right] and target > nums[mid]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #     return -1

    # 如果   target == right:
    #           return right
    #    elif  target <right
    #        if target == mid return
    #        else if target>mid or mid>right 从右侧查找
    #           else 从左侧查找
    #     else
    #        if target == mid return
    #        if target<mid or mid<right 从左侧侧
    #           else 从右侧查找
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target == nums[right]:
                return right
            elif target < nums[right]:
                if target == nums[mid]:
                    return mid
                elif target > nums[mid] or nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                if target == nums[mid]:
                    return mid
                elif target < nums[mid] or nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right
        return -1


# @lc code=end

sol = Solution()
res = sol.search([1, 3, 5], 5)
print(res)
