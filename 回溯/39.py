'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def combinationSum(self, candidates, target):
        # sort
        candidates.sort()
        size = len(candidates)
        path = []
        res = []
        self.dfs(candidates, 0, size, path, res, target)
        return res

    def dfs(self, candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path[:])
        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:
                break

            path.append(candidates[index])
            self.dfs(candidates, index, size, path, res, residue)
            path.pop()

    def combinationSum2(self, candidates, target: int):
        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        path = []
        res = []
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            res.append(path[:])

        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，索引起始还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()


if __name__ == '__main__':
    sol = Solution()
    max = sol.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
    print(max)
