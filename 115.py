'''
115. 不同的子序列
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
dp[i][j]指以i,j为底的result
dp[i][0]=0
s[i]==t[j] dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
s[i]!=t[j] dp[i][j]=dp[i-1][j]
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m + 1)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

                




sol = Solution()
res = sol.numDistinct("rabbbit", "rabbit")
print(str(res))
