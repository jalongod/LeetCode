'''
97. 交错字符串
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
动态规划
dp[i][j]以s1[i]和s2[j]为底的两个字符串是否组成了s3[i+j]
dp[i][j] = (dp[i-1][j] && s3[i+j-1] == s1[i-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1])
'''


class Solution2:  # 动态规划
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]

        dp[0][0] = True
        # 第一行
        for j in range(1, l2 + 1):
            dp[0][j] = (dp[0][j - 1] and s2[j - 1] == s3[j - 1])

        # 第一列
        for i in range(1, l1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


class Solution:  # 回溯 超时
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def isInter(s1, s2, s3):
            nonlocal res
            l1, l2, l3 = len(s1), len(s2), len(s3)
            # print("l1={0},l2={1},l3={2}".format(s1, s2, s3))
            if l1 == 0 and l2 == 0 and l3 == 0:
                res = True
                return

            if l1 > 0 and l3 > 0 and s1[0] == s3[0]:
                node = s1.pop(0)
                s3.pop(0)
                isInter(s1, s2, s3)
                s1.insert(0, node)
                s3.insert(0, node)
            l3 = len(s3)
            if l2 > 0 and l3 > 0 and s2[0] == s3[0]:
                node = s2.pop(0)
                s3.pop(0)
                isInter(s1, s2, s3)
                s2.insert(0, node)
                s3.insert(0, node)

        res = False
        isInter(list(s1), list(s2), list(s3))
        return res


sol = Solution2()
res = sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")
print(str(res))
# res = sol.isInterleave("aabcc", "dbbca", "aadbbbaccc")
# print(str(res))
# res = sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")
# print(str(res))
res = sol.isInterleave("a", "b", "a")
print(str(res))
