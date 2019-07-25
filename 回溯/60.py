'''
60. 第k个排列

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        tmp = [0] * n
        for j in range(n):
            tmp[j] = j + 1
        res = []

        def __factorial(n):
            # 这种编码方式包括了 0 的阶乘是 1 这种情况
            res = 1
            while n:
                res *= n
                n -= 1
            return res

        def bt(array, node, depth, path):
            nonlocal k
            nonlocal res
            if len(path) == n:
                return ''.join(str(i) for i in path)
            ps = __factorial(n - 1 - depth)

            for node in tmp:
                if node in path:
                    continue
                if ps < k:
                    k -= ps
                    continue
                path.append(node)
                return bt(tmp, node, depth + 1, path)

        return bt(tmp, None, 0, [])


if __name__ == '__main__':
    sol = Solution()
    max = sol.getPermutation(9, 94626)
    print(max)