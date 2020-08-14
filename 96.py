'''
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
'''
'''
dp[i]:i个节点的树的个数
dp[i]=[dp[j]+dp[i-j-1]if i-j-1!=j else dp[j] for j in range(i)] #左边j个，右边i-j-1个
'''


class Solution:
    def numTrees2(self, n):
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]

    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1  # i个节点的个数
        for i in range(2, n + 1):
            for j in range(0, i):  # j 是左边节点的个数 j从0到i-1 右边节点的个数为i-j-1
                if dp[j] < 1:
                    dp[i] += dp[i - j - 1]
                elif dp[i - j - 1] < 1:
                    dp[i] += dp[j]
                else:
                    dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]


sol = Solution()
max = sol.numTrees(4)

print(max)
