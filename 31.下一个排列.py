#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.31%)
# Likes:    347
# Dislikes: 0
# Total Accepted:    36.2K
# Total Submissions: 111.4K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


# 1234 1243
# 13452 13524
# 1.这道题没有介绍什么是字典序，建议百度了解下，不然只看题会没思路
# 设计思路：
# 1.从数组右侧向左开始遍历，找是否存在nums[i]>nums[i-1]的情况，
# 2.如果不存在这种nums[i]>nums[i-1]情况 ，for循环会遍历到i==0（也就是没有下一个排列），此时按题意排成有序Arrays.sort()
# 3.如果存在，则将从下标i到nums.length()的部分排序，然后在排过序的这部分中遍历找到第一个大于nums[i-1]的数，并与nums[i-1]交换位置


from typing import List


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(nums):
            pass

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            


# @lc code=end
