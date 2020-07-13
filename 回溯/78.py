'''
78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums):
        if not nums:
            return []

        def bt(first):
            res.append(path[:])
            if first == len(nums):
                return
            for index in range(first, len(nums)):
                path.append(nums[index])
                bt(index + 1)
                path.pop()
            pass

        res, path = [], []
        bt(0)
        return res

    # dp
    # dp 定义以i为结尾的子串的子集
    # dp公式 dp[i] = dp[i-1]+ [node+nums[i] for node in dp[i-1]]

    def subsets2(self, nums):
        dp = [[]]
        for i in range(len(nums)):
            dp = dp + [node + [nums[i]] for node in dp]
        return dp
        pass

    # 递归
    def subsets3(self, nums):
        if len(nums) == 0:
            return [[]]
        return self.subsets3(nums[:-1]) + [
            node + [nums[-1]] for node in self.subsets3(nums[:-1])
        ]
        pass


if __name__ == '__main__':
    sol = Solution()
    max = sol.subsets([1, 2, 3])
    # max = sol.subsets2([1, 2, 3])
    # max = sol.subsets3([1, 2, 3])
    print(max)