'''74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        # 查找行
        top, bottom = 0, len(matrix) - 1
        while top + 1 < bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] == target:
                return True
                break
            elif matrix[mid][0] > target:
                bottom = mid
            else:
                top = mid
        row = 0
        if matrix[bottom][0] <= target:
            row = bottom
        else:
            row = top
        # 查找列
        left, right = 0, len(matrix[0]) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid
            else:
                left = mid
        if matrix[row][left] == target or matrix[row][right] == target:
            return True
        return False


sol = Solution()
# max = sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 30)
max = sol.searchMatrix([[]], 1)

print(max)
