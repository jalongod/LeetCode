'''
全排列 2

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def permuteUnique(self, nums):
        if not nums:
            return []
        self.res = []
        self.per(nums, len(nums), [], [])
        return self.res

    def per(self, nums, size, path, used):
        if len(path) == size:
            self.res.append(path[:])
            return
        for index in range(0, len(nums)):
            if not index == nums.index(nums[index]):
                continue
            path.append(nums[index])
            tmp = nums.pop(index)
            self.per(nums, size, path, used)
            path.pop()
            nums.insert(index, tmp)
        pass


if __name__ == '__main__':
    sol = Solution()
    max = sol.permuteUnique([1, 1, 2])  # false
    # max = sol.permuteUnique([1, 2, 3])  # false
    print(max)