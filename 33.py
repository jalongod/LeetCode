'''
33. 搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = -1
        if not nums or len(nums) <= 0:
            return res

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target > nums[right]:
                if target < nums[mid] or nums[mid] <= nums[right]:
                    right = mid
                elif target == nums[mid]:
                    return mid
                else:
                    left = mid
            else:
                if target > nums[mid] or nums[mid] > nums[right]:
                    left = mid
                elif target == nums[mid]:
                    return mid
                else:
                    right = mid
        if target == nums[left]:
            res = left
        elif target == nums[right]:
            res = right
        return res


sol = Solution()
# max = sol.search([3, 4, 5, 1, 2], 3)
max = sol.search([5, 1, 3], 5)
print(max)
