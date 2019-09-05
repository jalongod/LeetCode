'''
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s2 = ''
        for i in reversed(s):
            s2 += i
        return s == s2
        # s1 = reversed(s)
        # s = str(x)
        # i = 0
        # stack = []
        # while i < len(s) // 2:
        #     stack.append(s[i])
        #     i += 1
        # if len(s) & 1 == 1:
        #     i += 1
        # while i < len(s):
        #     if stack.pop() != s[i]:
        #         return False
        #     i += 1
        # return len(stack) == 0


sol = Solution()
max = sol.isPalindrome(12)
print(max)
