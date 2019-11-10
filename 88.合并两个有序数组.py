#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        # nums1[:]=[]
        p1, p2 = 0, 0
        while(p1 < m and p2 < n):
            if nums1_copy[p1] <= nums2[p2]:
                nums1[p1+p2] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p1+p2] = nums2[p2]
                p2 += 1
        if p1 == m:
            while(p2 < n):
                nums1[p1+p2] = nums2[p2]
                p2 += 1
        else:
            while(p1 < m):
                nums1[p1+p2] = nums1_copy[p1]
                p1 += 1
        a = 1


# @lc code=end

sol = Solution()
sol.merge([-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 5, [-1, -1, 0, 0, 1, 2], 6)
