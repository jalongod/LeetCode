'''
77. 组合

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def combine(self, n: int, k: int):
        if k <= 0:
            return []
        res = []

        def dfs(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()

        dfs(1, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    max = sol.combine(20, 16)
    print(max)