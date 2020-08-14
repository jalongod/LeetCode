#
# @lc app=leetcode.cn id=1072 lang=python3
#
# [1072] 按列翻转得到最大值等行数
#

# @lc code=start
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def getCount(row):
            res, cnt, cur = [], 1, row[0]
            for i in range(len(row)):
                if cur == num:
                    cnt += 1
                else:
                    res.append(str(cnt))
                    cur = num
                    cnt = 1
            return "".join(res)

        dic = {}
        res = 0
        for row in matrix:
            feature = getCount(row)
            dic[feature] = dic[feature] + 1 if dic.__contains__(feature) else 1
            res = max(res, dic[feature])
        return res


# @lc code=end

sol = Solution()
res = sol.maxEqualRowsAfterFlips([[0, 1], [1, 1]])
print(res)
"""
000
001
110

110
111
000
"""