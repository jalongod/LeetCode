'''
全排列


给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''


class Solution:
    def permute(self, nums):
        if not nums:
            return []
        self.res = []
        self.per(nums, 0, len(nums), [])
        return self.res

    def per(self, nums, begin, size, path):
        if len(path) == size:
            self.res.append(path[:])
            return
        for index in range(begin, size):
            if nums[index] in path:
                continue
            path.append(nums[index])
            self.per(nums, 0, size, path)
            path.pop()
        pass


if __name__ == '__main__':
    sol = Solution()
    # max = sol.permute([1, 1, 2])  # false
    max = sol.permute([1, 2, 3])  # false
    print(max)