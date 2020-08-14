'''
11. 盛最多水的容器

'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, res = 0, len(height) - 1, 0
        while (left < right):
            cap = (right - left) * min(height[left], height[right])
            res = max(res, cap)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return res


sol = Solution()
# max = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
max = sol.maxArea([1, 2, 4, 3])

print(max)
