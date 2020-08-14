#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (42.71%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    19.2K
# Total Submissions: 44.7K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
#
# 提示：
#
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
#
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？
#
#

from typing import List

# 这个题目的重点是：
# 有两种清理方式：1清理超出窗口范围的第一个节点 2清理小于当前节点的所有节点
# 第一种清理：要用节点的下标来清理
# 第二种清理：通过比较窗口中的值来清理
# 所以：窗口内要保存节点下标


# @lc code=start
class Solution:
    # 双端队列
    # def cdequeue()
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        res, dq = [], deque()
        if len(nums) == 0 or k < 2:
            return nums
        for i in range(len(nums)):
            # 清理超出窗口的首节点
            if dq and dq[0] <= i - k:
                dq.popleft()
            # 清理小于当前节点的所有节点
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


# @lc code=end

sol = Solution()
sol.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3)
