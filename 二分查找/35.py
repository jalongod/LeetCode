'''
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def searchInsert(self, nums, target) -> int:
        left, right = 0, len(nums) - 1
        mid = -1
        add = False
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                add = True
            else:
                right = mid - 1
                add = False
        return mid + 1 if add else mid


sol = Solution()
max = sol.searchInsert([1, 3, 5, 6], 7)
print(max)
