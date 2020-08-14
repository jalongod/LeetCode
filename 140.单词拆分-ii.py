#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if not wordDict:
            return []

        set1 = set(list(s))
        set2 = set(list("".join(wordDict)))
        if set1 - set2:
            return []

        res = []
        max_length = len(max(wordDict, key=len))

        # # 递归
        # def recur(s, wordDict, preStr):
        #     if s == "" or not s:
        #         res.append(preStr)
        #         return
        #     right = min(max_length, len(s))
        #     for i in range(1, right + 1):
        #         if s[:i] in wordDict:
        #             nextStr = s[:i] if preStr == "" else preStr + " " + s[:i]
        #             recur(s[i:], wordDict, nextStr)

        # recur(s, wordDict, "")

        # dp
        dp = [[] for _ in range(len(s) + 1)]
        for i in range(0, len(s) + 1):
            word = s[:i]
            if word in wordDict:
                dp[i].append(word)
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                word = s[j:i]
                if len(dp[j]) and word in wordDict:
                    parr = dp[j]
                    for k in range(len(parr)):
                        dp[i].append(parr[k] + " " + word)
        return res


# @lc code=end

sol = Solution()
res = sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print(res)
