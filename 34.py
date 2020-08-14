'''
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if len(nums) <= 0 or not nums:
            return res
        left, right = 0, len(nums) - 1
        # 查找第一个位置
        while (left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            res[0] = left
        elif nums[right] == target:
            res[0] = right

        left, right = 0, len(nums) - 1
        # 查找第一个位置
        while (left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            res[1] = right
        elif nums[left] == target:
            res[1] = left
        return res


sol = Solution()
# max = sol.searchRange([5, 7, 7, 8, 8, 10], 6)
max = sol.searchRange([1], 0)
print(max)
