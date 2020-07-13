#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (36.05%)
# Likes:    312
# Dislikes: 0
# Total Accepted:    39.5K
# Total Submissions: 109.7K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#

from typing import List


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d1, d2, res = {}, set(), []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s in d1:
                    li = d1.get(s)
                    li.append([i, j])
                    d1.pop(s)
                    d1.setdefault(s, li)
                else:
                    li = []
                    li.append([i, j])
                    d1.setdefault(s, li)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                n = target - s
                if n in d1:
                    li = d1.get(n)
                    for p2 in li:
                        m, n = p2[0], p2[1]
                        if i != m and i != n and j != m and j != n:
                            tmp = []
                            tmp.append(nums[i])
                            tmp.append(nums[j])
                            tmp.append(nums[m])
                            tmp.append(nums[n])
                            tmp.sort()
                            d2.add(','.join([str(x) for x in tmp]))
        for item in d2:
            ar = []
            for s in item.split(','):
                ar.append(int(s))
            res.append(ar)

        return res
        pass


# @lc code=end

sol = Solution()
res = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
print(res)
