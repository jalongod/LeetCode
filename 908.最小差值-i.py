#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#


# @lc code=start
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        # 方案1

        # max = 0
        # min = 10000
        # for n in A:
        #     if n > max:
        #         max = n
        #     if n < min:
        #         min = n
        # if max - min > K * 2:
        #     return max - min - K * 2
        # else:
        #     return 0

        #方案2
        return max(0, max(A) - min(A) - K * 2)


# @lc code=end
