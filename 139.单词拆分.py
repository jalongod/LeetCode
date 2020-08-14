#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if j == 4:
                    a = 1
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


# @lc code=end

sol = Solution()
res = sol.wordBreak("leetcode", ["leet", "code"])
print(res)
