'''
72. 编辑距离
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')


示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
'''
方法 1：动态规划
dp[i][j] 表示 word1 的前 i 个字母和 word2 的前 j 个字母之间的编辑距离。

dp[0][0] == 0
dp[0][1] == 0
dp[1][0] == 0

如果w1[i]==w2[j]，dp[i][j]=dp[i-1][j-1]
否则 如果dp[i][j]= min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1

'''


class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        if not w1 and not w2:
            return 0
        w1l = len(w1)
        w2l = len(w2)
        dp = [[0 for _ in range(w2l + 1)] for __ in range(w1l + 1)]

        for i in range(0, w1l + 1):
            for j in range(0, w2l + 1):
                if i == 0 and j == 0:
                    dp[0][0] = 0
                    continue
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                if w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j],
                                   dp[i - 1][j - 1]) + 1
        return dp[w1l][w2l]


sol = Solution()
res = sol.minDistance("intention", "execution")
print(str(res))
