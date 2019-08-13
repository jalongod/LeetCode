'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


'''
# 定义dp
#       dp[i][j] 表示字符串从i到j是否为回文串
#       即：
# dp初值
#       dp[i][i]=true
# dp公式
#       if(s[i]==s[j]&&dp[i-1][j+1])
#          dp[i][j]==true


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.res = ""

        def helper(i, j):
            while (i >= 0 and j < n and s[i] == s[j]):
                i -= 1
                j += 1
            if len(self.res) < j - i - 1:
                self.res = s[i + 1:j]

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_len = 1
        n = len(s)
        start = 0
        for i in range(1, n):
            even = s[i - max_len:i + 1]
            odd = s[i - max_len - 1:i + 1]
            #print(even,odd)
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
            elif i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1

        #print(start,max_len)
        return s[start:start + max_len]


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        res = ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        for i in range(n):
            for j in range(i + 1):  # 冒泡
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                if dp[j][i] and max_len < i + 1 - j:
                    res = s[j:i + 1]
                    max_len = i + 1 - j

        return res


sol = Solution3()
max = sol.longestPalindrome("cbbd")
print(max)
