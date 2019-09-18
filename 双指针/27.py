'''
27. 移除元素

'''

from typing import List


class Solution:
    def removeElement2(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n


sol = Solution()
max = sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(max)