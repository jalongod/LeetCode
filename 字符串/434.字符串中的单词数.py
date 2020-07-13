#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (33.06%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 35.9K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# 示例:
#
# 输入: "Hello, my name is John"
# 输出: 5
#
#
#


# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        ar = list(s)
        if not ar or not len(ar):
            return 0
        for i in range(len(s)):
            if i == 0:
                dp[0] = 1 if ar[0] != ' ' else 0
                continue
            if (ar[i] == ' ') or (ar[i] != ' ' and ar[i - 1] != ' '):
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + 1
        return dp[len(s) - 1]


# @lc code=end
sol = Solution()
print(sol.countSegments("   "))
