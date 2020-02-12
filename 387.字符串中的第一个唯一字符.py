#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (42.15%)
# Likes:    176
# Dislikes: 0
# Total Accepted:    59.4K
# Total Submissions: 137.8K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.
#
#
#
#
# 注意事项：您可以假定该字符串只包含小写字母。
#
#


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res, memo = -1, dict()
        for ch in s:
            if ch in memo:
                memo[ch] = 0
            else:
                memo.setdefault(ch, 1)
        for i in range(len(s)):
            if memo[s[i]] == 1:
                return i
        return res


# @lc code=end

sol = Solution()
res = sol.firstUniqChar("z")
print(res)
