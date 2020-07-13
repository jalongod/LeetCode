#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (48.60%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    22.8K
# Total Submissions: 46.3K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
#
#
#


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        l1, l2 = len(num1), len(num2)
        array1, array2 = list(num1), list(num2)

        def addTwoStr(i, add):
            if i >= l1 and i >= l2 and add == 0:
                return
            sum = add
            if i < l1:
                sum += int(array1[l1 - i - 1])
            if i < l2:
                sum += int(array2[l2 - i - 1])
            res.insert(0, sum % 10)
            addTwoStr(i + 1, 1 if sum >= 10 else 0)

        addTwoStr(0, 0)
        return ''.join(str(i) for i in res)


# @lc code=end

sol = Solution()
print(sol.addStrings("1", "9"))
