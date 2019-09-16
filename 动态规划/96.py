'''
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
'''

'''
dp[i]:i个节点的树的个数
dp[i]=[dp[j]+dp[i-j-1]if i-j-1!=j else dp[j] for j in range(i)] #左边j个，右边i-j-1个
'''

class Solution:
    def numTrees(self, n):
        dp = [0]*(n+1)
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]


sol = Solution()
    # max = sol.restoreIpAddresses("25525511135")
max = sol.numTrees(4)

print(max)
# if __name__ == '__main__':
#     sol = Solution()
#     # max = sol.restoreIpAddresses("25525511135")
#     max = sol.numTrees(3)

#     print(max)


