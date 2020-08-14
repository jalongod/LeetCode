'''
220. 存在重复元素 III
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    # 线性查找，O(n*min(k,n)) 超时
    def containsNearbyAlmostDuplicate(self, nums, k, t) -> bool:
        for i in range(1, len(nums)):
            for j in range(1, k + 1):
                if i - j >= 0:
                    if abs(nums[i] - nums[i - j]) <= t:
                        return True
                else:
                    break
        return False


sol = Solution()
# len = sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
# len = sol.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
len = sol.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
print(str(len))
